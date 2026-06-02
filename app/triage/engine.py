"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

import uuid
import hashlib

from app.core import logger, settings
from app.preprocessing import TextCleaner
from app.vectorstore import EmbeddingModel, MilvusClient
from app.search import ElasticClient
from app.cache import RedisClient
from app.llm import RetryHandler
from app.observability import Timer



class TriageEngine:

    """
    Main orchestration engine for support ticket triaging.
    """

    def __init__(self) -> None:

        """
        Initialize system services and dependencies.
        """

        self.cleaner = TextCleaner()

        self.milvus = MilvusClient()

        self.elastic = ElasticClient()

        self.redis = RedisClient()

        self.retry_handler = RetryHandler()


    def process_ticket(self, raw_ticket: str):

        """
        Process incoming support ticket through:
        - preprocessing
        - exact cache lookup
        - semantic cache lookup
        - LLM generation

        Args:
            raw_ticket (str):
                Raw incoming support ticket text.

        Returns:
            dict:
                Ticket analysis result with source metadata.
        """

        logger.info("New ticket received")

        cleaned_ticket = self.cleaner.clean(raw_ticket)

        cache_key = hashlib.md5(cleaned_ticket.encode()).hexdigest()

        try:

            with Timer("redis_lookup"):
                exact_cache = self.redis.get(cache_key)

            if exact_cache:
                logger.info(
                    "redis_cache_hit",
                    extra={
                        "source": "redis"})

                return {
                    "source": "redis",
                    "data": exact_cache,}

        except Exception:

            logger.exception("redis_lookup_failed")

        with Timer("embedding_generation"):
            embedding = EmbeddingModel.encode(cleaned_ticket)

        try:
            with Timer("milvus_search"):
                results = self.milvus.search(embedding)

            if results:

                hit = results[0][0]

                similarity = hit.distance

                logger.info(f"Similarity score: {similarity}")

                threshold = (
                    settings.HIGH_CONFIDENCE_THRESHOLD if len(cleaned_ticket) < 20 else settings.SIMILARITY_THRESHOLD)

                if similarity >= threshold:
                    ticket_id = hit.id
                    logger.info(f"Semantic cache hit {ticket_id}")

                    with Timer("elastic_retrieval"):
                        cached_data = (self.elastic.get_ticket(ticket_id))

                    return {"source": "semantic_cache",
                             "data": cached_data,}

        except Exception as e:
            logger.exception("Semantic cache failed")

        logger.info("LLM generation started")

        with Timer("llm_generation"):
            analysis = (self.retry_handler.generate_with_retry(cleaned_ticket))

        ticket_id = str(uuid.uuid4())

        document = {
            "ticket_id": ticket_id,
            "question": cleaned_ticket,
            "analysis": analysis.model_dump(),
        }

        try:
            self.elastic.save_ticket(ticket_id, document,)

        except Exception:
            logger.exception("Failed to save to Elastic")

        try:
            self.milvus.insert(ticket_id, embedding,)

        except Exception:
            logger.exception("Failed to insert into Milvus")

        try:
            self.redis.set(cache_key, str(document),)

        except Exception:
            logger.exception("Filed to write Redis cache")
            
        return {
            "source": "llm",
            "data": document,}
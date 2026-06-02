"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

from pymilvus import connections, Collection

from app.core import logger, settings

class MilvusClient:

    """
    Milvus semantic vector search client.
    """

    def __init__(self):

        """
        Initialize Milvus connection and collection.
        """

        try:
            connections.connect(
                alias="default",
                host=settings.MILVUS_HOST,
                port=settings.MILVUS_PORT,)

            self.collection = Collection("support_cache")

            logger.info("Connected to Milvus")

        except Exception as e:

            logger.exception("Milvus connection failed")

            raise e

    def search(self, embedding):

        """
        Search for semantically similar embeddings.

        Args:
            embedding (list):
                Query vector embedding.

        Returns:
            list:
                Similarity search results.
        """

        try:
            results = self.collection.search(
                data=[embedding],
                anns_field="embedding",
                param={
                    "metric_type": "COSINE",
                    "params": {"ef": 128}},
                limit=1,)

            return results

        except Exception as e:

            logger.exception("Milvus search failed")

            raise e

    def insert(self, ticket_id, embedding):

        """
        Store ticket embedding in Milvus.

        Args:
            ticket_id (str):
                Unique ticket identifier.

            embedding (list):
                Vector embedding representation.
        """

        try:
            self.collection.insert([
                [ticket_id],
                [embedding],])

            logger.info(f"Milvus insert success {ticket_id}")

        except Exception as e:

            logger.exception("Milvus insert failed")

            raise e
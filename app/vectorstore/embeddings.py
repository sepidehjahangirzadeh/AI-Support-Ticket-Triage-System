"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

from sentence_transformers import SentenceTransformer

from app.core import logger


class EmbeddingModel:

    """
    Embedding model wrapper using BAAI/bge-m3.
    """

    _model = None

    @classmethod
    def get_model(cls):

        """
        Load embedding model once as singleton.
        """

        if cls._model is None:

            logger.info("Loading BAAI/bge-m3 model")

            cls._model = SentenceTransformer("BAAI/bge-m3")

        return cls._model

    @classmethod
    def encode(cls, text: str):

        """
        Generate normalized vector embedding.

        Args:
            text (str):
                Input ticket text.

        Returns:
            list:
                Vector embedding representation.
        """

        try:
            model = cls.get_model()

            embedding = model.encode(text, normalize_embeddings=True,)

            return embedding.tolist()

        except Exception as e:

            logger.exception("Embedding generation failed")

            raise e
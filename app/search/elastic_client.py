"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""


from elasticsearch import Elasticsearch

from app.core import logger, settings


class ElasticClient:

    """
    Elasticsearch client for ticket storage and retrieval.
    """

    def __init__(self):

        """
        Initialize Elasticsearch connection.
        """

        self.client = Elasticsearch(settings.ELASTIC_HOST)

    def save_ticket(self, ticket_id, document):

        """
        Store ticket data in Elasticsearch.

        Args:
            ticket_id (str):
                Unique ticket identifier.

            document (dict):
                Structured ticket document.
        """

        try:
            self.client.index(
                index="support_tickets",
                id=ticket_id,
                document=document,)

            logger.info(f"Elastic save success {ticket_id}")

        except Exception as e:

            logger.exception("Elastic save failed")

            raise e

    def get_ticket(self, ticket_id):

        """
        Retrieve ticket document by ID.

        Args:
            ticket_id (str):
                Unique ticket identifier.

        Returns:
            dict:
                Stored ticket document.
        """

        try:
            result = self.client.get(
                index="support_tickets",
                id=ticket_id,)

            return result["_source"]

        except Exception as e:

            logger.exception("Elastic retrieval failed")

            raise e
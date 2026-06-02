"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""


import time

from app.core import logger, settings
from app.llm import LLMClient, StructuredParser


class RetryHandler:
    """
    Handles retry logic for LLM generation failures.
    """

    def __init__(self):
        
        """
        Initialize LLM client.
        """

        self.client = LLMClient()

    def generate_with_retry(self, ticket: str):

        """
        Generate structured ticket analysis with retry support.

        Args:
            ticket (str):
                Cleaned support ticket text.

        Returns:
            TicketAnalysis:
                Validated structured output.

        Raises:
            Exception:
                If all retry attempts fail.
        """

        last_exception = None

        for attempt in range(settings.MAX_RETRIES):

            try:
                logger.info(
                    f"LLM attempt {attempt + 1}")

                response = self.client.generate(ticket)

                parsed = StructuredParser.parse(response)

                logger.info("LLM generation success")

                return parsed

            except Exception as e:

                last_exception = e

                logger.error(f"Attempt failed: {str(e)}")

                time.sleep(2)

        logger.exception("All retries failed")

        raise Exception(f"LLM failed after retries: {last_exception}")
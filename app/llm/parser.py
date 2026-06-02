"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

from pydantic import ValidationError

from app.models import TicketAnalysis
from app.core import StructuredOutputError


class StructuredParser:
    """
    Validates and parses structured LLM outputs.
    """

    @staticmethod
    def parse(output: str):
        """
        Parse LLM JSON output into TicketAnalysis schema.

        Args:
            output (str):
                Raw JSON response from the LLM.

        Returns:
            TicketAnalysis:
                Validated structured ticket analysis.

        Raises:
            StructuredOutputError:
                If schema validation fails.
        """

        try:
            return TicketAnalysis.model_validate_json(output)

        except ValidationError as e:

            raise StructuredOutputError(str(e))
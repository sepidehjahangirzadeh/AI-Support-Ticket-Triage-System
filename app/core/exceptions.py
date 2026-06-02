"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

class LLMGenerationError(Exception):
    """
    Raised when LLM generation fails.
    """

    def __init__(
        self,
        message="LLM generation failed",
        provider=None,
    ):

        self.message = message
        self.provider = provider

        super().__init__(self.message)


class StructuredOutputError(Exception):
    """
    Raised when LLM output validation fails.
    """

    def __init__(
        self,
        message="Invalid structured output",
        raw_output=None,
    ):

        self.message = message
        self.raw_output = raw_output

        super().__init__(self.message)


class VectorSearchError(Exception):
    """
    Raised when semantic vector search fails.
    """

    def __init__(
        self,
        message="Vector search failed",
        collection=None,
    ):

        self.message = message
        self.collection = collection

        super().__init__(self.message)


class ElasticFailure(Exception):
    """
    Raised when Elasticsearch operations fail.
    """

    def __init__(
        self,
        message="Elasticsearch operation failed",
        index=None,
    ):

        self.message = message
        self.index = index

        super().__init__(self.message)
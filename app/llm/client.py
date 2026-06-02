"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from app.core import settings
from app.llm.prompts import TRIAGE_PROMPT


class LLMClient:
    """
    LangChain-based Groq LLM client.

    Handles prompt orchestration and ticket analysis generation.
    """

    def __init__(self):
        
        """
        Initialize Groq LLM client.
        """

        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model="llama-3.1-8b-instant",
            temperature=0,
            max_tokens=250,)

    def generate(self, ticket: str):

        """
        Generate structured analysis for a support ticket.

        Args:
            ticket (str):
                Cleaned support ticket text.

        Returns:
            str:
                Raw LLM response content.
        """

        prompt = ChatPromptTemplate.from_template(TRIAGE_PROMPT)

        chain = prompt | self.llm

        response = chain.invoke(
            {
                "ticket": ticket
            })

        return response.content
"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    APP_NAME: str = "Support-Triage-Engine"

    GROQ_API_KEY: str

    ELASTIC_HOST: str

    MILVUS_HOST: str
    MILVUS_PORT: str

    REDIS_HOST: str
    REDIS_PORT: int

    SIMILARITY_THRESHOLD: float = 0.90

    HIGH_CONFIDENCE_THRESHOLD: float = 0.97

    MAX_RETRIES: int = 3

    LOG_LEVEL: str = "INFO"

    class Config:
        """
        Pydantic environment configuration.
        """

        env_file = ".env"


settings = Settings()
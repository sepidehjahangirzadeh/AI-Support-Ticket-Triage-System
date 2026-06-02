"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

import logging

import redis

from app.core import settings


class RedisClient:
    """
    Redis exact-match cache client.

    Handles fast cache retrieval for repeated tickets
    to reduce LLM calls and latency.
    """

    def __init__(self):
        """
        Initialize Redis connection.
        """

        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,
        )

    def get(self, key):
        """
        Retrieve cached value by key.
        """
        return self.client.get(key)

    def set(self, key, value):
        """
        Store value in Redis cache.
        """
        self.client.set(key, value)
"""
Support Triaging Engine

Author: Sepideh Jahangirzadeh
َ"""

import time

from app.core import logger

class Timer:
    """
    Context manager for latency monitoring.

    ```
    Example:
        with Timer("redis_lookup"):
            redis.get(key)
    """

def __init__(self, operation: str):

    self.operation = operation
    self.start_time = None

def __enter__(self):

    self.start_time = time.perf_counter()

    return self

def __exit__(self, exc_type, exc_val,exc_tb,):

    latency_ms = (time.perf_counter() - self.start_time) * 1000

    logger.info(
        "operation_latency",
        extra={
            "operation": self.operation,
            "latency_ms": round(
                latency_ms,
                2,
            ),
        },
    )

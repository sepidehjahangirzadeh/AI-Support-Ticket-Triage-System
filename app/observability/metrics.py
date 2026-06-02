"""
Observability and monitoring utilities.

This module is responsible for:
- metrics collection
- tracing
- latency monitoring
- operational visibility

Why observability matters:
AI systems involve multiple distributed components:
- Redis
- Milvus
- Elasticsearch
- LLM providers

Without observability:
- debugging becomes difficult
- bottlenecks become invisible
- production incidents become harder to diagnose

This layer improves production reliability.
"""
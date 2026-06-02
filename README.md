# Support Triaging Engine

Production-ready AI-powered support ticket routing system.

## Author

sepideh jahangirzadeh

# ___________________________________________________________________________________

## PRODUCTION FLOW
Client Request
    ↓
Preprocessing
    ↓
Redis Exact Cache
    ↓
Embedding Generation
    ↓
Milvus Semantic Search
    ↓
Elastic Retrieval
    ↓
If Miss → LLM
    ↓
Pydantic Validation
    ↓
Retry + Repair
    ↓
Save to Redis
    ↓
Save to Elastic
    ↓
Save to Milvus

# ___________________________________________________________________________________
## PRODUCTION FEATURES

FastAPI Microservice
LangChain Orchestration
Structured Output Validation
Retry Handling
Anti-Hallucination Prompt
Redis Hot Cache
Milvus Semantic Cache
Elasticsearch Retrieval
BAAI/bge-m3 Embeddings
Excel-based Preprocessing Rules
Logging
Exception Handling
Dockerized Infrastructure
Production-ready Architecture
Singleton Embedding Model
Dynamic Similarity Thresholds
Semantic Deduplication
Token Optimization
# _____________________________________________________________________________________________
## PRODUCTION FLOW

Client Request
    ↓
Preprocessing
    ↓
Redis Exact Cache
    ↓
Embedding Generation
    ↓
Milvus Semantic Search
    ↓
Elastic Retrieval
    ↓
If Miss → LLM
    ↓
Pydantic Validation
    ↓
Retry + Repair
    ↓
Save to Redis
    ↓
Save to Elastic
    ↓
Save to Milvus
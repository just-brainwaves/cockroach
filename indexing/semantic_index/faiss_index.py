"""
Module  : indexing.semantic_index.faiss_index
Purpose : FAISS-backed vector index for Phase 1 local deployments.
          Manages IVFFlat index creation, upsert, cosine similarity search,
          and on-disk persistence under VECTOR_DB_PATH.
Layer   : Indexing — Vector Search (Phase 1)
"""

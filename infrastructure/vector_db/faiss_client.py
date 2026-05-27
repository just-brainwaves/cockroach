"""
Module  : infrastructure.vector_db.faiss_client
Purpose : FAISS IVFFlat vector index client for local Phase-1 deployments.
          Wraps faiss-cpu with: async-safe access mutex, on-disk persistence,
          and a simple upsert(id, vector) / search(query, k) interface.
Layer   : Infrastructure — Vector Database (Phase 1)
"""

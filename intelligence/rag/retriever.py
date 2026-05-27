"""
Module  : intelligence.rag.retriever
Purpose : Semantic retrieval engine for the RAG pipeline.
          Queries the vector index (FAISS/Qdrant) with a query embedding,
          applies metadata pre-filters (language, file type, project),
          and returns ranked candidate chunks for LLM context injection.
Layer   : Intelligence — RAG Pipeline
"""

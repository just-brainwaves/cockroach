"""
Module  : intelligence.rag.pipeline
Purpose : End-to-end RAG pipeline orchestration.
          Composes: query_embed → retrieve → rerank → context_assemble → generate.
          Supports streaming output and source citation tracking.
Layer   : Intelligence — RAG Pipeline
"""

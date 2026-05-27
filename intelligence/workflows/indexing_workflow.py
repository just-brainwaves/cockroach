"""
Module  : intelligence.workflows.indexing_workflow
Purpose : LangGraph workflow orchestrating the repository indexing pipeline.
          Nodes: scan → parse → embed → build_graph → build_semantic_index.
          Designed for partial failure recovery and incremental re-indexing.
Layer   : Intelligence — LangGraph Workflow
"""

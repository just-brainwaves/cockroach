"""
Module  : intelligence.workflows.debug_workflow
Purpose : Main LangGraph workflow for full debugging investigations.
          Node sequence: context_retrieval → multi_agent_dispatch →
          hypothesis_merge → confidence_ranking → recommendation_gen.
          Deterministic, stateful, and auditable — every step is logged.
Layer   : Intelligence — LangGraph Workflow (Core)
"""

"""
Module  : intelligence.workflows.root_cause_workflow
Purpose : Dedicated LangGraph workflow for root cause analysis.
          Implements a progressive narrowing strategy: broad anomaly space
          → causal chain tracing → commit attribution → fix suggestion.
          This workflow IS the primary product differentiator.
Layer   : Intelligence — LangGraph Workflow (Core Moat)
"""

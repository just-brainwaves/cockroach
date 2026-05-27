"""
Module  : intelligence.rag.context_builder
Purpose : Context window assembly for LLM prompts.
          Packs retrieved code chunks, graph context, and runtime signals
          into a structured prompt within token budget constraints.
          Uses MMR (Maximal Marginal Relevance) to balance relevance and diversity.
Layer   : Intelligence — RAG Pipeline
"""

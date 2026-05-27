"""
Module  : indexing.chunking.semantic_chunker
Purpose : Splits source files into semantically meaningful embedding units.
          Prefers function/class/block boundaries over token-count splits.
          Each chunk carries metadata needed for RAG attribution and graph lookup.
Layer   : Indexing — Embedding Preparation
"""

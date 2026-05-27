"""
Module  : intelligence.embeddings.code_chunker
Purpose : Intelligent code chunking for embedding generation.
          Splits source files at AST boundaries (functions, classes, blocks)
          rather than fixed token windows, preserving syntactic completeness.
          Each chunk carries metadata: file path, symbol name, language, line range.
Layer   : Intelligence — Semantic Understanding
"""

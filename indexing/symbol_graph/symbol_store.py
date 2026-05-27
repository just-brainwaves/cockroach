"""
Module  : indexing.symbol_graph.symbol_store
Purpose : Persists extracted symbols to Postgres (structured lookup) and
          the vector DB (semantic search). Maintains symbol → file → project
          mappings and supports fast "find all callers of X" queries.
Layer   : Indexing — Symbol Intelligence
"""

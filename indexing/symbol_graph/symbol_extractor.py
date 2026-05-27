"""
Module  : indexing.symbol_graph.symbol_extractor
Purpose : Normalises and qualifies symbols extracted from ASTs.
          Produces fully-qualified names (module.Class.method), source locations,
          type signatures, and visibility (public/private/exported) for Neo4j ingestion.
Layer   : Indexing — Symbol Intelligence
"""

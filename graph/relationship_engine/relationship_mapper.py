"""
Module  : graph.relationship_engine.relationship_mapper
Purpose : Maps raw indexing output to semantically typed Neo4j relationships.
          Routes dependency edges to the correct relationship type:
          IMPORTS, CALLS, INHERITS, IMPLEMENTS, USES, TESTS, CONFIGURES.
Layer   : Graph — Relationship Intelligence
"""

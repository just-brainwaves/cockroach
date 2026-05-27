"""
Module  : infrastructure.neo4j.schema
Purpose : Neo4j schema bootstrap and constraint definitions.
          Declares node labels: File, Symbol, Module, Service.
          Declares relationship types: IMPORTS, CALLS, INHERITS, IMPLEMENTS.
          Creates uniqueness constraints and indexes on startup for query performance.
Layer   : Infrastructure — Graph Database Schema
"""

SCHEMA_SETUP_QUERIES = [
    "CREATE CONSTRAINT file_path_unique IF NOT EXISTS FOR (f:File) REQUIRE f.path IS UNIQUE",
    "CREATE CONSTRAINT symbol_fqn_unique IF NOT EXISTS FOR (s:Symbol) REQUIRE s.fqn IS UNIQUE",
    "CREATE INDEX file_project_idx IF NOT EXISTS FOR (f:File) ON (f.project_id)",
]

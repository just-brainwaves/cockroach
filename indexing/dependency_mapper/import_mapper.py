"""
Module  : indexing.dependency_mapper.import_mapper
Purpose : Resolves import/require/use statements to concrete file targets.
          Builds the inter-file dependency edges written to Neo4j as IMPORTS
          relationships. Handles relative imports, aliased imports, and monorepo paths.
Layer   : Indexing — Dependency Intelligence
"""

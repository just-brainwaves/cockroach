"""
Module  : tests.conftest
Purpose : Shared pytest fixtures for the Cockroach test suite.
          Provides: async DB session (test Postgres), Neo4j test driver,
          FAISS in-memory index, mock Celery app, and fixture repositories.
Layer   : Tests — Shared Fixtures
"""
import pytest

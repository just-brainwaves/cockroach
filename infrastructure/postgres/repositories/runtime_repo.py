"""
Module  : infrastructure.postgres.repositories.runtime_repo
Purpose : Postgres repository for runtime telemetry records.
          Stores normalised log entries, trace metadata, crash events,
          and anomaly records with project/time indexing for fast retrieval.
Layer   : Infrastructure — Repository Pattern
"""

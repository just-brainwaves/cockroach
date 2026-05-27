"""
Module  : infrastructure.postgres.repositories.analysis_repo
Purpose : Postgres repository for Analysis sessions and Finding records.
          Supports bulk insert of findings, paginated history retrieval,
          and atomic status updates during streaming agent execution.
Layer   : Infrastructure — Repository Pattern
"""

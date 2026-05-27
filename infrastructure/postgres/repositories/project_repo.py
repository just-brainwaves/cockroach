"""
Module  : infrastructure.postgres.repositories.project_repo
Purpose : Postgres repository for the Project aggregate.
          Implements: create, get_by_id, list_by_user, update_status, delete.
          Uses SQLAlchemy async ORM — all methods are awaitable.
Layer   : Infrastructure — Repository Pattern
"""

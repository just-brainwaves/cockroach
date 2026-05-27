"""
Module  : infrastructure.postgres.migrations.env
Purpose : Alembic migration environment. Wires SQLAlchemy models to Alembic,
          configures async migration support, and sets the metadata target
          for auto-generated schema diff migrations.
Layer   : Infrastructure — Database Migrations
"""

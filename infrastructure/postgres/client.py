"""
Module  : infrastructure.postgres.client
Purpose : Async PostgreSQL client using SQLAlchemy 2.0 + asyncpg driver.
          Provides async session factory, connection pool management,
          and a health-check probe used by the API lifespan handler.
Layer   : Infrastructure — Primary Database
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

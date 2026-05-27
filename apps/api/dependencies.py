"""
Module  : apps.api.dependencies
Purpose : FastAPI dependency injection providers.
          Yields scoped async DB sessions, resolves authenticated user context
          from JWT, and provides lazily-initialized service singletons.
Layer   : Application — Dependency Injection
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()


async def get_db_session():
    """Yield an async SQLAlchemy session, rolling back on error."""
    ...


async def get_current_user(token=Depends(security)):
    """Decode JWT and return the authenticated user entity."""
    ...

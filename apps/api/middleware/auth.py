"""
Module  : apps.api.middleware.auth
Purpose : JWT authentication middleware.
          Validates Bearer tokens on every protected route,
          decodes user identity, and attaches it to request.state.
Layer   : Application — Security
"""
from starlette.middleware.base import BaseHTTPMiddleware

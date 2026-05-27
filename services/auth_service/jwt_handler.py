"""
Module  : services.auth_service.jwt_handler
Purpose : JWT encode/decode/refresh utilities.
          Issues signed access tokens (15 min TTL) and refresh tokens (7 day TTL).
          Validates signature, expiry, and token revocation status via Redis.
Layer   : Services — Security
"""

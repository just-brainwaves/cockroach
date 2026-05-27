"""
Module  : infrastructure.redis.client
Purpose : Async Redis client factory using redis-py async.
          Creates a connection pool shared by: Celery broker, cache layer,
          and pub/sub event bus. Provides health-check and graceful shutdown.
Layer   : Infrastructure — Cache / Message Broker
"""
import redis.asyncio as redis

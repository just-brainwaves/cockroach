"""
Module  : infrastructure.redis.cache
Purpose : Application-level typed caching layer over Redis.
          Provides get/set/invalidate/bulk_invalidate with TTL management.
          Caches: expensive graph queries, embedding lookups, AI response fragments.
Layer   : Infrastructure — Cache
"""

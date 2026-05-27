"""
Module  : infrastructure.redis.pubsub
Purpose : Redis pub/sub event bus for real-time domain event broadcasting.
          Publishers (services, workers) push domain events to named channels.
          Subscribers (API SSE endpoints, WebSocket handlers) consume and forward.
Layer   : Infrastructure — Event Bus
"""

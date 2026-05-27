"""
Module  : domain.contracts.notifier
Purpose : Abstract contract for event notification. Decouples domain event publishing from specific transport (Redis, WebSocket, email).
Layer   : Domain — Interface Contract
"""
from abc import ABC, abstractmethod

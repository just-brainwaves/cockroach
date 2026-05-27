"""
Module  : domain.contracts.indexer
Purpose : Abstract contract for repository indexers. Any indexing strategy (local, remote, incremental) must implement this.
Layer   : Domain — Interface Contract
"""
from abc import ABC, abstractmethod

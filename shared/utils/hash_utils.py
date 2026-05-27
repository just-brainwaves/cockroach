"""
Module  : shared.utils.hash_utils
Purpose : Hashing utilities for content-addressable indexing and cache keys.
          Generates stable SHA-256 hashes for: file contents, AST node fingerprints,
          embedding cache keys, and analysis context deduplication.
Layer   : Shared — Utilities
"""
import hashlib


def sha256(content: str | bytes) -> str:
    if isinstance(content, str):
        content = content.encode()
    return hashlib.sha256(content).hexdigest()

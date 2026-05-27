"""
Module  : intelligence.embeddings.embedder
Purpose : Core embedding generation service.
          Uses sentence-transformers (bge-large-en-v1.5 by default) to convert
          code chunks, error messages, and docstrings to dense vectors.
          Supports batched generation and GPU acceleration when available.
Layer   : Intelligence — Semantic Understanding
"""


class Embedder:
    """Wraps sentence-transformers with batching, caching, and model switching."""

    def __init__(self, model_name: str = "BAAI/bge-large-en-v1.5"):
        ...

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a list of text chunks."""
        ...

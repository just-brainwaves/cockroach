"""
Module  : intelligence.embeddings.models
Purpose : Embedding model registry and loader.
          Manages local model downloads to ~/.cache/cockroach/models,
          GPU vs CPU selection, and provides a unified interface across
          bge-large, e5-large, and nomic-embed-text.
Layer   : Intelligence — Model Management
"""

SUPPORTED_MODELS = {
    "bge-large":    "BAAI/bge-large-en-v1.5",
    "e5-large":     "intfloat/e5-large-v2",
    "nomic-embed":  "nomic-ai/nomic-embed-text-v1.5",
}

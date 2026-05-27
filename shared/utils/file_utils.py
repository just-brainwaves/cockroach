"""
Module  : shared.utils.file_utils
Purpose : File system utility functions used across the indexing layer.
          Provides: safe path resolution, .gitignore rule parsing,
          recursive directory walk with extension filter, binary file detection.
Layer   : Shared — Utilities
"""
import os
from pathlib import Path

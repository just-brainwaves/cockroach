"""
Module  : shared.constants.languages
Purpose : Supported language definitions and extension → language ID mappings.
          Used by the parser registry, graph schema, and embedding model selection.
Layer   : Shared — Constants
"""

SUPPORTED_LANGUAGES: dict[str, str] = {
    ".py":   "python",
    ".ts":   "typescript",
    ".tsx":  "typescript",
    ".js":   "javascript",
    ".jsx":  "javascript",
    ".rs":   "rust",
    ".go":   "go",
    ".java": "java",
    ".cpp":  "cpp",
    ".cc":   "cpp",
    ".c":    "c",
    ".h":    "c",
}

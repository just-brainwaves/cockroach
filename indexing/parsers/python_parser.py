"""
Module  : indexing.parsers.python_parser
Purpose : Python source parser using tree-sitter.
          Extracts classes, functions, decorators, type annotations, async patterns, and context managers.
Layer   : Indexing — AST Parsing
"""
from indexing.parsers.base_parser import BaseParser, ParseResult

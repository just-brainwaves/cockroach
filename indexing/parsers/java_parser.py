"""
Module  : indexing.parsers.java_parser
Purpose : Java source parser using tree-sitter.
          Extracts classes, Spring bean annotations, synchronization primitives, and dependency injection patterns.
Layer   : Indexing — AST Parsing
"""
from indexing.parsers.base_parser import BaseParser, ParseResult

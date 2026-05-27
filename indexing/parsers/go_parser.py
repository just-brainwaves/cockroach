"""
Module  : indexing.parsers.go_parser
Purpose : Go source parser using tree-sitter.
          Extracts goroutines, channels, select blocks, interfaces, and sync primitives critical for concurrency analysis.
Layer   : Indexing — AST Parsing
"""
from indexing.parsers.base_parser import BaseParser, ParseResult

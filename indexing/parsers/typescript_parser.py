"""
Module  : indexing.parsers.typescript_parser
Purpose : Typescript source parser using tree-sitter.
          Handles TSX/JSX, extracts React components, hooks, interfaces, and module exports.
Layer   : Indexing — AST Parsing
"""
from indexing.parsers.base_parser import BaseParser, ParseResult

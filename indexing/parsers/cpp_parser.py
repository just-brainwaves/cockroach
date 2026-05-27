"""
Module  : indexing.parsers.cpp_parser
Purpose : Cpp source parser using tree-sitter.
          Extracts classes, templates, virtual methods, and memory management calls (new/delete/malloc/free).
Layer   : Indexing — AST Parsing
"""
from indexing.parsers.base_parser import BaseParser, ParseResult

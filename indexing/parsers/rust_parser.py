"""
Module  : indexing.parsers.rust_parser
Purpose : Rust source parser using tree-sitter.
          Extracts structs, enums, traits, impl blocks, unsafe regions, and lifetime annotations for memory safety analysis.
Layer   : Indexing — AST Parsing
"""
from indexing.parsers.base_parser import BaseParser, ParseResult

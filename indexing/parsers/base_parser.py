"""
Module  : indexing.parsers.base_parser
Purpose : Abstract base class for all language parsers.
          Contract: parse(source, path) → ParseResult with AST, symbols, imports.
          All parsers register themselves in the registry via a decorator.
Layer   : Indexing — AST Parsing
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class ParseResult:
    file_path: str
    language: str
    symbols: list[dict] = field(default_factory=list)    # functions, classes, vars
    imports: list[dict] = field(default_factory=list)    # import → resolved path
    calls: list[dict]   = field(default_factory=list)    # call site → target
    ast_hash: str = ""                                   # content fingerprint


class BaseParser(ABC):
    @abstractmethod
    def parse(self, source_code: str, file_path: str) -> ParseResult: ...

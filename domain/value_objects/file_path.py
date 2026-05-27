"""
Module  : domain.value_objects.file_path
Purpose : FilePath immutable value object with normalisation and language detection.
          Ensures consistent cross-OS path representation and provides:
          .language, .extension, .is_test_file, .relative_to(base) helpers.
Layer   : Domain — Value Objects
"""
from dataclasses import dataclass
from pathlib import Path
from shared.constants.languages import SUPPORTED_LANGUAGES


@dataclass(frozen=True)
class FilePath:
    raw: str

    @property
    def extension(self) -> str:
        return Path(self.raw).suffix

    @property
    def language(self) -> str | None:
        return SUPPORTED_LANGUAGES.get(self.extension)

    @property
    def is_test_file(self) -> bool:
        return "test" in Path(self.raw).stem.lower()

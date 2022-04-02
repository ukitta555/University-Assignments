import logging
from decimal import Decimal
from typing import Any
logger = logging.getLogger(__name__)


class SegmentReader:
    def __init__(self):
        self.segments: list[tuple[Decimal]] = []

    def run(self, filename: str, **kwargs) -> Any:
        with open(filename, 'r') as file:
            for line in file:
                segment = SegmentReader._parse_coordinates(line)
                self._add_segment(segment)
        return self.segments

    def _add_segment(self, segment: tuple[Decimal]):
        self.segments.append(segment)
        logger.info(f"Saved segment {segment}")

    @staticmethod
    def _parse_coordinates(line_of_text: str) -> tuple[Decimal]:
        return convert_tokens_to_coordinates(line_of_text.split())


def convert_tokens_to_coordinates(raw_numbers_from_file: list[str]) -> tuple[Decimal]:
    return tuple(map(Decimal, raw_numbers_from_file))
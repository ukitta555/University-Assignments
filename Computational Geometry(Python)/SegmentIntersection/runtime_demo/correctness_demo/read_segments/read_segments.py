import logging
from typing import TextIO, Any

from interface import implements

from runtime_demo.utils.smart_file.callback_that_uses_file import CallbackThatUsesFile
from runtime_demo.utils.smart_file.no_file_provided_exception import NoFileProvidedException
from runtime_demo.utils.type_aliases import QtSegment

logger = logging.getLogger(__name__)


class ReadSegments(implements(CallbackThatUsesFile)): # type: ignore
    def __init__(self):
        self.segments: list[QtSegment] = []

    def run(self, file_handler: TextIO = None, **kwargs) -> Any:
        if file_handler:
            for line in file_handler:
                segment = ReadSegments._parse_coordinates(line)
                self._add_segment(segment)
        else:
            raise NoFileProvidedException()
        return self.segments

    def _add_segment(self, segment):
        self.segments.append(segment)
        logger.info(f"Saved segment {segment}")

    @staticmethod
    def _parse_coordinates(line_of_text: str) -> tuple[float]:
        return ReadSegments._convert_tokens_to_coordinates(
            ReadSegments._get_raw_tokens(line_of_text)
        )

    @staticmethod
    def _convert_tokens_to_coordinates(raw_numbers_from_file: list[str]) -> tuple[float]:
        return tuple(map(float, raw_numbers_from_file))

    @staticmethod
    def _get_raw_tokens(line_of_text: str) -> list[str]:
        return line_of_text.split()

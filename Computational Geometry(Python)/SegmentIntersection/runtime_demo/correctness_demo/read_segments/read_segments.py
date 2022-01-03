import logging
from typing import TextIO, Any

from interface import implements

from runtime_demo.utils.smart_file.callback_that_uses_file import CallbackThatUsesFile
from runtime_demo.utils.smart_file.no_file_provided_exception import NoFileProvidedException
from runtime_demo.utils.type_aliases import Segment

logger = logging.getLogger(__name__)


class ReadSegments(implements(CallbackThatUsesFile)): # type: ignore
    def __init__(self):
        self.segments: list[Segment] = []

    def run(self, file_handler: TextIO = None, **kwargs) -> Any:
        if file_handler:
            for line in file_handler:
                segment = ReadSegments._parse_segment_from_text_(line)
                self._add_segment_(segment)
        else:
            raise NoFileProvidedException()
        return self.segments

    def _add_segment_(self, segment):
        self.segments.append(segment)
        logger.info(f"Saved segment {segment}")

    @staticmethod
    def _parse_segment_from_text_(line_of_text) -> Segment:
        return Segment(*ReadSegments._parse_coordinates_(line_of_text))

    @staticmethod
    def _parse_coordinates_(line_of_text: str) -> list[float]:
        return ReadSegments._convert_tokens_to_coordinates_(
            ReadSegments._get_raw_tokens_(line_of_text)
        )

    @staticmethod
    def _convert_tokens_to_coordinates_(raw_numbers_from_file: list[str]) -> list[float]:
        result = []
        for number in raw_numbers_from_file:
            result.append(float(number))
        return result

    @staticmethod
    def _get_raw_tokens_(line_of_text: str) -> list[str]:
        return line_of_text.split()

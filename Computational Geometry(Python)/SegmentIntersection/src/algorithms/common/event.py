from src.utils.computational_types import MySegment


class Event:
    _segments: list[MySegment] = []

    def __init__(self, segment):
        self._segments.append(segment)
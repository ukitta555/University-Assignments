import os

import pytest

from runtime_demo.utils.type_aliases import RawSegment, SegmentForMockFile


def stringify_segment(segment: RawSegment):
    return SegmentForMockFile(*segment).__str__()


def get_stringified_segments(segments: list[RawSegment]):
    stringified_segments = []
    for segment in segments:
        stringified_segments.append(stringify_segment(segment))
    return stringified_segments


@pytest.fixture
def mock_file_with_segment_data(mock_segments):
    filename = 'mock.txt'
    with open(filename, 'x+') as f:
        f.writelines(get_stringified_segments(mock_segments))
    yield filename
    os.remove(filename)

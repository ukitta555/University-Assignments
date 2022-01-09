import os

import pytest

from runtime_demo.utils.type_aliases import RawSegment, SegmentForMockFile, QtSegment


def float_coordinates(segment):
    return tuple(map(float, segment))


@pytest.fixture
def mock_segments():
    mock_segments: list[RawSegment] = [
        (0.0, 0.0, 100.0, 100.0),
        (0.0, 100.0, 100.0, 0.0)
    ]
    # sanity check - converting everything to float
    return list(map(float_coordinates, mock_segments))


def stringify_segment(segment: RawSegment):
    return SegmentForMockFile(*segment).__str__()


def get_stringified_segments(segments: list[RawSegment]):
    stringified_segments = []
    for segment in segments:
        stringified_segments.append(stringify_segment(segment))
    return stringified_segments


@pytest.fixture
def mock_file_with_mock_segment_data(mock_segments):
    filename = 'mock.txt'
    with open(filename, 'x+') as f:
        f.writelines(get_stringified_segments(mock_segments))
    yield filename
    os.remove(filename)

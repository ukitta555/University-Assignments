import pytest

from runtime_demo.utils.type_aliases import RawSegment


def float_coordinates(segment):
    return tuple(map(float, segment))


@pytest.fixture
def mock_segments():
    mock_segments: list[RawSegment] = [
        (0.0, 0.0, 2.0, 2.0),
        (0.0, 2.0, 2.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.5, 0.0),
    ]
    # sanity check - converting everything to float
    return list(map(float_coordinates, mock_segments))
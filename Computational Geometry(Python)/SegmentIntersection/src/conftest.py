from decimal import Decimal

import pytest
from PyQt5.QtCore import QLineF

from utils.computational_types import RawSegment


def decimal_coordinates(segment):
    return tuple(map(Decimal, segment))


@pytest.fixture
def mock_segments():
    mock_segments: list[RawSegment] = [
        (0.0, 0.0, 2.0, 2.0),
        (0.0, 2.0, 2.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.5, 0.0),
    ]
    # sanity check - converting everything to Decimal
    return list(map(decimal_coordinates, mock_segments))


class SegmentForMockFile(QLineF):
    def __eq__(self, other):
        x1 = self.x1() == other.x1()
        x2 = self.x2() == other.x2()
        y1 = self.y1() == other.y1()
        y2 = self.y2() == other.y2()
        return x1 and x2 and y1 and y2

    def __str__(self):
        return f"{self.x1()} {self.y1()} {self.x2()} {self.y2()}\n"
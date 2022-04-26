from decimal import Decimal
from typing import Tuple

import pytest
from PyQt5.QtCore import QLineF

from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import RawSegment


def decimal_coordinates(segment) -> tuple[Decimal, Decimal, Decimal, Decimal]:
    return (
            Decimal(segment[0]),
            Decimal(segment[1]),
            Decimal(segment[2]),
            Decimal(segment[3]),
    )

@pytest.fixture
def mock_segments():
    mock_segments: list[RawSegment] = [
        (0.0, 0.0, 2.0, 2.0),
        (0.0, 2.0, 2.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (1.0, 0.0, 1.5, 0.0),
    ]
    return list(map(decimal_coordinates, mock_segments))

@pytest.fixture
def sentinel_scientific_segments():
    sentinels = [
        (-20000.0, 20000.0, -20000.0, -20000.0),  # left sentinel
        (20000.0, 20000.0, 20000.0, -20000.0)  # right sentinel
    ]
    return convert_to_scientific(list(map(decimal_coordinates, sentinels)))

@pytest.fixture
def scientific_mock_segments(mock_segments):
    return convert_to_scientific(mock_segments)


class SegmentForMockFile(QLineF):
    def __eq__(self, other):
        x1 = self.x1() == other.x1()
        x2 = self.x2() == other.x2()
        y1 = self.y1() == other.y1()
        y2 = self.y2() == other.y2()
        return x1 and x2 and y1 and y2

    def __str__(self):
        return f"{self.x1()} {self.y1()} {self.x2()} {self.y2()}\n"
import pytest

from src.conftest import decimal_coordinates
from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import RawSegment


@pytest.fixture
def order_fix_segments():
    mock_segments: list[RawSegment] = [
        (0.0, 0.0, 4.0, 4.0),
        (1.0, 0.0, 3.0, 4.0),
        (3.0, 0.0, 1.0, 4.0),
        (4.0, 0.0, 0.0, 4.0),
    ]
    return convert_to_scientific(list(map(decimal_coordinates, mock_segments)))
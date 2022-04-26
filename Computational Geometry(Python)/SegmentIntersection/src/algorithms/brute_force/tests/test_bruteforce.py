from src.algorithms.brute_force.brute_force_solution import find_intersections_slow
from src.algorithms.common.intersection import Intersection
from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import MySegment, MyPoint


class TestBruteforceCorrectness:
    def test_bruteforce_correctness(self, mock_segments):
        intersections = find_intersections_slow(convert_to_scientific(mock_segments))
        assert len(intersections) == 3
        assert intersections == {MyPoint(1, 1), MyPoint(0, 0), MyPoint(1, 0)}
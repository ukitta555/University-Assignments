from sympy import Point2D

from algorithms.brute_force.brute_force_solution import find_intersections_slow
from algorithms.intersection import Intersection
from runtime_demo.correctness_demo.utils.utils import convert_to_scientific
from runtime_demo.utils.type_aliases import SymPySegment, SymPyPoint2D


class TestBruteforceCorrectness:
    def test_bruteforce_correctness(self, mock_segments):
        intersections = find_intersections_slow(convert_to_scientific(mock_segments))
        assert len(intersections) == 3
        assert intersections == [
            Intersection(
                SymPyPoint2D(1, 1),
                SymPySegment(SymPyPoint2D(0, 0), SymPyPoint2D(2, 2)),
                SymPySegment(SymPyPoint2D(2, 0), SymPyPoint2D(0, 2)),
            ),
            Intersection(
                SymPyPoint2D(0, 0),
                SymPySegment(SymPyPoint2D(0, 0), SymPyPoint2D(2, 2)),
                SymPySegment(SymPyPoint2D(0, 0), SymPyPoint2D(1, 0)),
            ),
            Intersection(
                SymPyPoint2D(1, 0),
                SymPySegment(SymPyPoint2D(0, 0), SymPyPoint2D(1, 0)),
                SymPySegment(SymPyPoint2D(1, 0), SymPyPoint2D(1.5, 0)),
            ),
        ]
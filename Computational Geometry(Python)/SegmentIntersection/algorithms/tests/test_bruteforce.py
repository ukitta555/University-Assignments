from algorithms.brute_force.brute_force_solution import find_intersections_slow
from algorithms.intersection import Intersection
from runtime_demo.correctness_demo.utils.utils import convert_to_scientific
from runtime_demo.utils.type_aliases import MySegment, MyPoint


class TestBruteforceCorrectness:
    def test_bruteforce_correctness(self, mock_segments):
        intersections = find_intersections_slow(convert_to_scientific(mock_segments))
        assert len(intersections) == 3
        assert intersections == [
            Intersection(
                MyPoint(1, 1),
                MySegment(MyPoint(0, 0), MyPoint(2, 2)),
                MySegment(MyPoint(2, 0), MyPoint(0, 2)),
            ),
            Intersection(
                MyPoint(0, 0),
                MySegment(MyPoint(0, 0), MyPoint(2, 2)),
                MySegment(MyPoint(0, 0), MyPoint(1, 0)),
            ),
            Intersection(
                MyPoint(1, 0),
                MySegment(MyPoint(0, 0), MyPoint(1, 0)),
                MySegment(MyPoint(1, 0), MyPoint(1.5, 0)),
            ),
        ]
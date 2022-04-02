from algorithms.brute_force.brute_force_solution import find_intersections_slow
from runtime_demo.correctness_demo.utils.utils import convert_to_scientific


class TestSweepLine:
    def test_sweepline(self, mock_segments):
        slow_intersections = find_intersections_slow(convert_to_scientific(mock_segments))
        fast_intersections = find_intersections_fast(convert_to_scientific(mock_segments))
        assert len(fast_intersections) == 3
        assert slow_intersections == fast_intersections

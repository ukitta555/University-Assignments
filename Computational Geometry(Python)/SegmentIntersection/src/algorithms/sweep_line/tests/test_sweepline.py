from decimal import Decimal

from src.algorithms.brute_force.brute_force_solution import find_intersections_slow
from src.algorithms.common.lcuevent import LCUEvent
from src.algorithms.sweep_line.sweep_line import SweepLine, find_intersections_fast
from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import SortedSet, MySegment, MyPoint, SortedDict


class TestSweepLine:
    def test_sweepline(self, scientific_mock_segments):
        slow_intersections = find_intersections_slow(scientific_mock_segments)
        fast_intersections = find_intersections_fast(scientific_mock_segments)
        assert len(fast_intersections) == 3
        assert slow_intersections == fast_intersections


    def test_queue_population_on_init(self, scientific_mock_segments):
        sweep_line = SweepLine()
        sweep_line._populate_event_queue_and_lcu_lists(scientific_mock_segments)
        event_queue: SortedDict[MyPoint, LCUEvent] = sweep_line.event_queue

        test_point = MyPoint(0, 0)
        assert event_queue[test_point].lower.__contains__(scientific_mock_segments[0])
        assert event_queue[test_point].upper.__contains__(scientific_mock_segments[2])
        test_point = MyPoint(1, 0)
        assert event_queue[test_point].lower.__contains__(scientific_mock_segments[2])
        assert event_queue[test_point].upper.__contains__(scientific_mock_segments[3])

    def test_event_processing_loop(self, scientific_mock_segments):
        segment_to_insert = scientific_mock_segments[0]
        sweep_line = SweepLine()
        sweep_line._populate_event_queue_and_lcu_lists([segment_to_insert])
        event_queue: SortedDict[MyPoint, LCUEvent] = sweep_line.event_queue

        counter = 0
        flag = True
        fake_intersection_point = MyPoint(1, 1)
        point_fetch_order = []
        while event_queue.is_not_empty():
            event_point = event_queue.get_next_event_point()
            point_fetch_order.append(event_point)
            event_queue.pop(event_point)
            if flag:
                event_queue[fake_intersection_point] = LCUEvent()
                flag = False
            counter += 1
        assert len(point_fetch_order) == 3
        assert point_fetch_order == [segment_to_insert.start, fake_intersection_point, segment_to_insert.end]

    def test_nearest_left(self, scientific_mock_segments, sentinel_scientific_segments):
        T = SortedSet()

        MySegment.set_sweep_level(Decimal(0))
        for seg in scientific_mock_segments + sentinel_scientific_segments:
            T.insert(seg)

        assert T.nearest_left_to_segment(scientific_mock_segments[2]) == scientific_mock_segments[3]
        assert T.nearest_left_to_segment(scientific_mock_segments[3]) == sentinel_scientific_segments[1]
        assert T.nearest_left_to_segment(sentinel_scientific_segments[1]) == scientific_mock_segments[1]
        assert T.nearest_left_to_segment(scientific_mock_segments[1]) == scientific_mock_segments[0]
        assert T.nearest_left_to_segment(scientific_mock_segments[0]) == sentinel_scientific_segments[0]
        assert T.nearest_left_to_segment(sentinel_scientific_segments[0]) is None

    def test_nearest_right(self, scientific_mock_segments, sentinel_scientific_segments):
        T = SortedSet()
        MySegment.set_sweep_level(0)
        for seg in scientific_mock_segments + sentinel_scientific_segments:
            T.insert(seg)

        assert T.nearest_right_to_segment(sentinel_scientific_segments[0]) == scientific_mock_segments[0]
        assert T.nearest_right_to_segment(scientific_mock_segments[0]) == scientific_mock_segments[1]
        assert T.nearest_right_to_segment(scientific_mock_segments[1]) == sentinel_scientific_segments[1]
        assert T.nearest_right_to_segment(sentinel_scientific_segments[1]) == scientific_mock_segments[3]
        assert T.nearest_right_to_segment(scientific_mock_segments[3]) is scientific_mock_segments[2]
        assert T.nearest_right_to_segment(scientific_mock_segments[2]) is None


    def test_rb_ordering(self, scientific_mock_segments, sentinel_scientific_segments):
        T = SortedSet()
        for seg in scientific_mock_segments + sentinel_scientific_segments:
            T.insert(seg)

        MySegment.set_sweep_level(Decimal(0))

        result = [
            sentinel_scientific_segments[0],
            scientific_mock_segments[0],
            scientific_mock_segments[1],
            sentinel_scientific_segments[1],
            scientific_mock_segments[3],
            scientific_mock_segments[2],
        ]
        for index, seg in enumerate(T):
            print(index)
            assert seg == result[index]

    def test_sweepline_order_fix(self, order_fix_segments):
        sweep_line = SweepLine()
        mock_sweep_line_tree: SortedSet[MySegment] = SortedSet()

        MySegment.set_sweep_level(Decimal(3.5))
        mock_event = LCUEvent()

        for segment in order_fix_segments:
            mock_sweep_line_tree.insert(segment)
            mock_event.add_to_C(segment)

        sweep_line.sweep_line_order_tree = mock_sweep_line_tree

        factual_initial_order = []
        for segment in sweep_line.sweep_line_order_tree:
            factual_initial_order.append(segment)

        expected_initial_order = order_fix_segments[::-1]

        assert factual_initial_order == expected_initial_order

        sweep_line._fix_sweep_line_ordering(MyPoint(2, 2), mock_event)

        expected_order = order_fix_segments
        for index, segment in enumerate(sweep_line.sweep_line_order_tree):
            assert expected_order[index] == segment

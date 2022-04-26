import logging
import time
from math import cos, sin
from decimal import Decimal
import random

from src.const import EPSILON
from src.algorithms.common.lcuevent import LCUEvent
from src.utils.computational_types import MySegment, MyPoint, SortedSet, SortedDict

logger = logging.getLogger(__name__)

# noinspection PyPep8Naming
class SweepLine:
    def __init__(self):
        self.event_queue: SortedDict[MyPoint, LCUEvent] = SortedDict()
        self.sweep_line_order_tree: SortedSet[MySegment] = SortedSet()
        self.intersections: set[MyPoint] = set()

    def sweep_intersections(self, segments: list[MySegment]):
        self._populate_event_queue_and_lcu_lists(segments)


        while self.event_queue.is_not_empty():
            event_point = self.event_queue.get_next_event_point()
            event = self.event_queue.pop(event_point)
            self._handle_event_point(event, event_point)

        return self.intersections

    def _populate_event_queue_and_lcu_lists(self, segments: list[MySegment]):
        for segment in segments:
            self._process_segment_starting_point(segment)
            self._process_segment_ending_point(segment)

    def _process_segment_starting_point(self, segment: MySegment):
        if self.event_queue.get(segment.start):
            lcu_event: LCUEvent = self.event_queue[segment.start]
        else:
            lcu_event: LCUEvent = LCUEvent()
            self.event_queue[segment.start] = lcu_event
        lcu_event.add_to_U(segment)

    def _process_segment_ending_point(self, segment: MySegment):
        if self.event_queue.get(segment.end):
            lcu_event: LCUEvent = self.event_queue[segment.end]
        else:
            lcu_event: LCUEvent = LCUEvent()
            self.event_queue[segment.end] = lcu_event
        lcu_event.add_to_L(segment)

    def _handle_event_point(
            self,
            event: LCUEvent,
            event_point: MyPoint
    ):
        if len(event.lower) + len(event.contains) + len(event.upper) > 1:
            self.intersections.add(event_point)
            # logger.info(f'Found intersection: {event_point}')

        self._fix_sweep_line_ordering(event_point, event)

        if len(event.upper) + len(event.contains) == 0:
            self._handle_dangling_point_case(event_point=event_point)
        else:
            self._handle_contained_point_case(event=event, event_point=event_point)

    def _fix_sweep_line_ordering(self, event_point: MyPoint, event: LCUEvent):
        for segment in event.lower:
            self.sweep_line_order_tree.remove(segment)

        for segment in event.contains:
            self.sweep_line_order_tree.remove(segment)
            # assert not self.sweep_line_order_tree.get(segment)


        MySegment.set_sweep_level(event_point.y - Decimal(0.000005))

        for segment in event.contains:
            # assert not self.sweep_line_order_tree.get(segment)
            self.sweep_line_order_tree.insert(segment)

        for segment in event.upper:
            self.sweep_line_order_tree.insert(segment)

    def _handle_dangling_point_case(
            self,
            event_point: MyPoint
    ):
        left_neighbour = self._nearest_left_to_point(point=event_point)
        right_neighbour = self._nearest_right_to_point(point=event_point)
        if left_neighbour and right_neighbour:
            self._find_new_event(left_neighbour, right_neighbour, event_point)

    def _handle_contained_point_case(
            self,
            event: LCUEvent,
            event_point: MyPoint
    ):
        rightest_C_segment = max(list(event.contains.keys()) + list(event.upper.keys()))
        leftest_C_segment = min(list(event.contains.keys()) + list(event.upper.keys()))

        left_neighbour = self.sweep_line_order_tree.nearest_left_to_segment(leftest_C_segment)
        right_neighbour = self.sweep_line_order_tree.nearest_right_to_segment(rightest_C_segment)

        if left_neighbour:
            self._find_new_event(left_neighbour, leftest_C_segment, event_point)
        if right_neighbour:
            self._find_new_event(right_neighbour, rightest_C_segment, event_point)

    def _nearest_left_to_point(self, point: MyPoint):
        fake_segment: MySegment = MySegment(
            point,
            MyPoint(point.x, point.y - EPSILON),
        )

        self.sweep_line_order_tree.insert(fake_segment)
        result = self.sweep_line_order_tree.nearest_left_to_segment(fake_segment)
        self.sweep_line_order_tree.insert(fake_segment)

        return result

    def _nearest_right_to_point(self, point: MyPoint):
        fake_segment: MySegment = MySegment(
            point,
            MyPoint(point.x, point.y - EPSILON),
        )

        self.sweep_line_order_tree.insert(fake_segment)
        result = self.sweep_line_order_tree.nearest_right_to_segment(fake_segment)
        self.sweep_line_order_tree.remove(fake_segment)

        return result

    def _find_new_event(
            self,
            this_segment: MySegment,
            that_segment: MySegment,
            event_point: MyPoint
    ):
        intersection = this_segment.intersection(that_segment)

        if intersection:
            intersection = intersection[0]

        if intersection and \
            (SweepLine._intersection_is_below_sweep_line(intersection, event_point) or
             SweepLine._intersection_is_to_the_right_of_the_sweepline_hitpoint(intersection, event_point)):

            intersection: MyPoint = MyPoint(intersection.x, intersection.y)

            self._process_new_event(intersection, that_segment, this_segment)

    def _process_new_event(self, intersection, that_segment, this_segment):
        if not self.event_queue.get(intersection):
            new_event = LCUEvent()
            self.event_queue[intersection] = new_event

        if this_segment.contains(intersection):
            self.event_queue[intersection].add_to_C(this_segment)
        if that_segment.contains(intersection):
            self.event_queue[intersection].add_to_C(that_segment)

    @staticmethod
    def _intersection_is_to_the_right_of_the_sweepline_hitpoint(intersection, sweep_line_hitpoint):
        return abs(intersection.y - sweep_line_hitpoint.y) < EPSILON and intersection.x > \
               sweep_line_hitpoint.x

    @staticmethod
    def _intersection_is_below_sweep_line(intersection: MyPoint, point: MyPoint):
        return intersection.y < point.y

    @staticmethod
    def random_rotation_if_horizontal_lines_are_present(segments):

        def horizontal_segment_present(segments: list[MySegment]):
            for seg in segments:
                if seg.start.y == seg.end.y:
                    return True
            return False

        def random_rotation(segments):
            angle: float = random.uniform(0.1, 0.12)

            def rotate_segment_with_respect_to_origin(segment):

                def rotate_point_with_respect_to_origin(point: MyPoint):
                    return MyPoint(
                        point.x * Decimal(cos(angle)) - point.y * Decimal(sin(angle)),
                        point.x * Decimal(sin(angle)) + point.y * Decimal(cos(angle)),
                    )

                return MySegment(
                    rotate_point_with_respect_to_origin(segment.start),
                    rotate_point_with_respect_to_origin(segment.end)
                )

            return [rotate_segment_with_respect_to_origin(segment) for segment in segments]

        while horizontal_segment_present(segments):
            segments = random_rotation(segments)
        return segments


def find_intersections_fast(segments: list[MySegment]):
    start = time.time()
    result = SweepLine().sweep_intersections(segments=segments)
    end = time.time()
    print("The time of execution of optimized algo is :", end - start)
    return result
        
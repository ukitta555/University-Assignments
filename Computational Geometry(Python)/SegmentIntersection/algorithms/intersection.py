from sympy import Point2D

from runtime_demo.utils.type_aliases import Segment


class Intersection:
    def __init__(self,
                 intersection: Point2D | None,
                 segment_1: Segment,
                 segment_2: Segment):
        self.intersection: Point2D | None = intersection
        self.segment1: Segment = segment_1
        self.segment2: Segment = segment_2

    def __repr__(self):
        if self.intersection:
            return f"{self.intersection.__repr__()}, {self.segment1.__repr__()}, {self.segment2.__repr__()}"
        return "None"

    def __eq__(self, other):
        intersection = self.intersection == other.intersection
        segment1 = self.segment1 == other.segment1
        segment2 = self.segment2 == other.segment2
        return intersection and segment1 and segment2

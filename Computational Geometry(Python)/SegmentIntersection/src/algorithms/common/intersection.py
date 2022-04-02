from src.utils.computational_types import MySegment, MyPoint


class Intersection:
    def __init__(
            self,
            intersection: MyPoint | None,
            segment_1: MySegment,
            segment_2: MySegment
    ):
        self.intersection: MyPoint | None = intersection
        self.segment1: MySegment = segment_1
        self.segment2: MySegment = segment_2

    def __str__(self):
        return f"{self.intersection.__str__()}, {self.segment1.__str__()}, {self.segment2.__str__()}"

    def __eq__(self, other):
        are_intersections_equal = self.intersection == other.intersection
        is_segment1_equal = self.segment1 == other.segment1
        is_segment2_equal = self.segment2 == other.segment2
        return are_intersections_equal and is_segment1_equal and is_segment2_equal

from runtime_demo.utils.type_aliases import RawSegment, Segment, Point2D


def to_endpoints(segment: RawSegment):
    return Point2D(segment[0], segment[1]), Point2D(segment[2], segment[3])


def convert_to_scientific(raw_segments: list[RawSegment]):
    return [Segment(*to_endpoints(seg)) for seg in raw_segments]

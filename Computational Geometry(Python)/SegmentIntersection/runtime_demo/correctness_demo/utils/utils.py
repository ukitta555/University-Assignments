from runtime_demo.utils.type_aliases import RawSegment, SymPySegment, SymPyPoint2D


def to_endpoints(segment: RawSegment):
    return SymPyPoint2D(segment[0], segment[1]), SymPyPoint2D(segment[2], segment[3])


def convert_to_scientific(raw_segments: list[RawSegment]):
    return [SymPySegment(*to_endpoints(seg)) for seg in raw_segments]

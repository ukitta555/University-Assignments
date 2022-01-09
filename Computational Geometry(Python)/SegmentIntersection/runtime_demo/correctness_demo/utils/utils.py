from runtime_demo.utils.type_aliases import RawSegment, SymPySegment


def to_endpoints(segment: RawSegment):
    return (segment[0], segment[1]), (segment[2], segment[3])


def convert_to_scientific(raw_segments: list[RawSegment]):
    return [SymPySegment(*to_endpoints(seg)) for seg in raw_segments]

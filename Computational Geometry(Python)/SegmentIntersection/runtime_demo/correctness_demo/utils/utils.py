from runtime_demo.utils.type_aliases import RawSegment, MySegment, MyPoint


def to_endpoints(segment: RawSegment):
    return MyPoint(segment[0], segment[1]), MyPoint(segment[2], segment[3])


def convert_to_scientific(raw_segments: list[RawSegment]):
    return [MySegment(*to_endpoints(seg)) for seg in raw_segments]

from algorithms.intersection import Intersection
from runtime_demo.utils.type_aliases import Segment, Point2D


def find_intersections_slow(segments: list[Segment]):
    result = []
    for i in range(0, len(segments) - 1):
        for j in range(i + 1, len(segments)):
            intersection_point = segments[i].intersection(segments[j])
            if intersection_point:
                intersection_point = Point2D(
                    intersection_point[0].x,
                    intersection_point[0].y
                )
                result.append(
                    Intersection(
                        intersection_point,
                        segments[i],
                        segments[j]
                    )
                )
    return result
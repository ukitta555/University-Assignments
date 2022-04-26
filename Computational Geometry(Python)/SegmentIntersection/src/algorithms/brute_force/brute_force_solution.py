import logging
import time


from src.algorithms.common.intersection import Intersection
from src.utils.computational_types import MySegment, MyPoint

logger = logging.getLogger(__name__)

def find_intersections_slow(segments: list[MySegment]):
    start = time.time()
    result: set[MyPoint] = set()
    for i in range(0, len(segments) - 1):
        for j in range(i + 1, len(segments)):
            intersection_point = segments[i].intersection(segments[j])
            if intersection_point:
                intersection_point = MyPoint(
                    intersection_point[0].x,
                    intersection_point[0].y
                )
                # logger.info(f'Found intersection: {intersection_point}')
                result.add(intersection_point)
    end = time.time()
    print("The time of execution of bruteforce algo is :", end - start)
    return result
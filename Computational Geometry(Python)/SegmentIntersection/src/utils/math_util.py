from src.utils.computational_types import Vector


def cross_2d(a: Vector, b: Vector):
    return a.x * b.y - a.y * b.x


def orientation(vertex: Vector, a: Vector, b: Vector):
    p1: Vector = a - vertex
    p2: Vector = b - vertex
    area = cross_2d(p1, p2)

    if area > 0:
        return 1  # counter clockwise <1,0> -> <1, 1> should return 1
    if area < 0:
        return -1   # clockwise
    return 0

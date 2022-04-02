import typing

from sympy import Point2D, Segment2D


class MySegment(Segment2D):
    def __eq__(self, other):
        one_way = self.p1 == other.p1 and self.p2 == other.p2
        another = self.p1 == other.p2 and self.p2 == other.p1
        return one_way or another


class MyPoint(Point2D):
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

RawSegment: typing.TypeAlias = tuple[float, float, float, float]



import typing

from sympy import Point2D, Segment2D


class MySegment(Segment2D):

    def __eq__(self, other):
        direct_order = self.p1 == other.p1 and self.p2 == other.p2
        reverse_order = self.p1 == other.p2 and self.p2 == other.p1
        return direct_order or reverse_order


class MyPoint(Point2D):
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



RawSegment: typing.TypeAlias = tuple[float, float, float, float]


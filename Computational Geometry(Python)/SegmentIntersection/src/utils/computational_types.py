import functools
import functools
import typing
from cmath import sqrt
from decimal import Decimal

from bintrees import FastRBTree
from sympy import Point2D, Segment2D
from sympy.core.numbers import ComplexInfinity, NaN

from src.utils.red_black_library import Deck


@functools.total_ordering
class MyPoint(Point2D):

    def __new__(cls, x: float, y: float, **kwargs):
        if type(x) is float:
            x = Decimal(x)
        if type(y) is float:
            y = Decimal(y)

        return Point2D.__new__(cls, x, y, **kwargs)

    def __eq__(self, other):
        return abs(self.x - other.x) < Decimal(0.00005) and abs(self.y - other.y) < Decimal(0.00005)

    def __hash__(self):
        return int(self.x * 31 + self.y)

    def __lt__(self, other):
        if self.y > other.y or (self.y == other.y and self.x < other.x):
            return True
        return False

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def scalar_multiply(self, scalar):
        return MyPoint(self.x * scalar, self.y * scalar)

    def magnitude(self):
        return sqrt((self.x*self.x) + (self.y*self.y))


Vector: typing.TypeAlias = MyPoint
RawSegment: typing.TypeAlias = tuple[Decimal, Decimal, Decimal, Decimal]


class SortedDict(Deck):
    def is_empty(self):
        return len(self) == 0

    def is_not_empty(self):
        return len(self) > 0

    def get_next_event_point(self):
        return next(self.iterkeys())


class SortedSet(FastRBTree):
    def insert(self, key, value=None):
        super().insert(key, 'sample')


    def nearest_right_to_segment(self, segment):
        return self._nonexact_ceiling(segment)

    def nearest_left_to_segment(self, segment):
        return self._nonexact_floor(segment)

    def _nonexact_floor(self, key):
        try:
            # return next(self.irange(maximum=key, inclusive=(True, False), reverse=True))
            exact_floor = super().ceiling_key(key)
            if exact_floor == key:
                return super().prev_key(key)
        except KeyError:
            return None

    def _nonexact_ceiling(self, key):
        try:
            # return next(self.irange(minimum=key, inclusive=(False, True), reverse=False))
            exact_ceiling = super().ceiling_key(key)
            if exact_ceiling == key:
                return super().succ_key(key)
        except KeyError:
            return None


@functools.total_ordering
class MySegment(Segment2D):
    sweep_level: Decimal = Decimal(1000000)

    def __eq__(self, other):
        if other is None:
            return False
        direct_order = self.p1 == other.p1 and self.p2 == other.p2
        reverse_order = self.p1 == other.p2 and self.p2 == other.p1
        return direct_order or reverse_order

    # def __hash__(self):
    #     return int(self.start.__hash__() * 31 + self.end.__hash__())

    def __lt__(self, other):
        if other is None:
            return False
        return self.sweep_x_value < other.sweep_x_value

    def __new__(cls, p1: MyPoint, p2: MyPoint, **kwargs):
        # start => higher y value
        # end => lower y value
        # sweep line goes from top to bottom => from higher values to lower values
        start, end = MySegment._order_points_by_y_coordinate(p1, p2)
        assert start.y > end.y or (start.y == end.y and start.x <=  end.x)

        return Segment2D.__new__(cls, start, end, **kwargs)

    @property
    def start(self) -> MyPoint:
        return self.p1

    @property
    def end(self) -> MyPoint:
        return self.p2


    def contains(self, entity_to_check):
        if type(entity_to_check) is MyPoint:
            if self.start == entity_to_check or self.end == entity_to_check:
                return False
            return super().contains(entity_to_check)
        else:
            return super().contains(entity_to_check)

    @property
    def sweep_x_value(self):
        """
        Return X coordinate of intersection between sweep line on point.y level and this segment
        """
        # ray = Ray2D(MyPoint(0, self.sweep_level), MyPoint(1, self.sweep_level))
        # intersection = ray.intersection(self)
        # if intersection:
        #     if type(intersection[0]) is Point2D:
        #         return intersection[0].x
        #
        #     if type(intersection[0]) is Segment2D:
        #         intersection = MySegment(
        #             intersection[0].p1,
        #             intersection[0].p2
        #         )
        #         return intersection.start.x
        # return 9999999999999999999

        direction: Vector = self.end - self.start

        try:
            t = (MySegment.sweep_level - self.start.y) / direction.y
            if type(t) is NaN or type(t) is ComplexInfinity:
                t = 9999999999999999999999999999999999999999999
        except Exception:
            t = 9999999999999999999999999999999999999999999

        return direction.x * t + self.start.x

    @classmethod
    def set_sweep_level(cls, sweep_level: Decimal):
        cls.sweep_level = sweep_level

    @staticmethod
    def _order_points_by_y_coordinate(p1: MyPoint, p2: MyPoint):
        if p2.y > p1.y or (p2.y == p1.y and p2.x < p1.x):
            start = MyPoint(p2.x, p2.y)
            end = MyPoint(p1.x, p1.y)
        else:
            start = MyPoint(p1.x, p1.y)
            end = MyPoint(p2.x, p2.y)
        return start, end



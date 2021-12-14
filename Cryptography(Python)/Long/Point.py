import copy as cp

# Recommended Parameters secp224k1


class Point:
    p = 2 ** 224 - 2 ** 32 - 2 ** 12 - 2 ** 11 - 2 ** 9 - 2 ** 7 - 2 ** 4 - 2 - 1
    a = 0
    b = 5

    @classmethod
    def inv(cls, n):
        return pow(n, cls.p - 2, cls.p)

    def __init__(self, x, y):
        self.x = x % Point.p
        self.y = y % Point.p

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __neg__(self):
        return Point(self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __add__(self, other):
        if self == ZERO:
            return cp.copy(other)
        if other == ZERO:
            return cp.copy(self)
        if self == -other:
            return cp.copy(ZERO)

        if self == other:
            k = (3 * self.x**2 + Point.a) * Point.inv(2 * self.y)
        else:
            k = (other.y - self.y) * Point.inv(other.x - self.x)

        k %= Point.p
        x = k*k - self.x - other.x
        y = k*(self.x - x) - self.y
        return Point(x, y)

    def __mul__(self, n):
        result = cp.copy(ZERO)
        point = cp.copy(self)
        # binary multiplication
        while n > 0:
            if n & 1:
                result += point
            point += point
            n >>= 1     # i.e. quick multiply by 2
        return result

    def __rmul__(self, n):
        return self * n

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


ZERO = Point(0, 0)
P = Point(
    int('A1455B33_4DF099DF_30FC28A1_69A467E9_E47075A9_0F7E650E_B6B7A45C', 16),
    int('7E089FED_7FBA3442_82CAFBD6_F7E319F7_C0B0BD59_E2CA4BDB_556D61A5', 16)
)

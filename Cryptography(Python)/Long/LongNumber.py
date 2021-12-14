from itertools import zip_longest
import copy as cp


class LongNumber:
    """Class represents long number and implement basic operations"""

    def __init__(self, s):
        self.digits = []
        sign = 1
        self.BASE = 10
        try:
            if s[0] == '-':
                sign = -1
                s = s[1:]
            for i in reversed(s):
                self.digits.append(sign * int(i))
        except TypeError:
            s = str(s)
            if s[0] == '-':
                sign = -1
                s = s[1:]
            for i in reversed(s):
                self.digits.append(sign * int(i))
        except IndexError:
            pass

    def __str__(self):
        return self.is_negative() * '-' + ''.join([str(abs(i)) for i in reversed(self.digits)])
        # return str(self.digits)

    def __repr__(self):
        return self.is_negative() * '-' + ''.join([str(abs(i)) for i in reversed(self.digits)])

    def negate(self):
        """All digits *-1"""
        self.digits = [-i for i in self.digits]

    def get_reversed_digits(self):
        """Returns reversed digits list"""
        return list(reversed(self.digits))

    def is_negative(self):
        """True if the number is negative"""
        for i in reversed(self.digits):
            if i < 0:
                return True
            if i > 0:
                return False
        return False

    def sign(self):
        if self.is_negative():
            return LongNumber('-1')
        else:
            return LongNumber('1')

    def abs(self):
        return self.sign() * self

    def normalize(self):
        """After operation some digit list elements may overflow numeric system base.
        Check all digits for overflow"""
        d = self.digits
        for i in range(0 , len(d), 1):
            self.digit_normalize(i)
        while len(self.digits) > 0 and self.digits[len(self.digits) - 1] == 0:
            self.digits.pop()

    def digit_normalize(self, pos):
        """Normalize digit on the 'pos' position"""
        c = 1
        if self.is_negative():
            c = -1
        #  123 = [1 2 3]
        sign_digit = c * self.digits[pos]
        digit_length = len(self.digits)
        if pos < len(self.digits) - 1:
            self.digits[pos + 1] += c * (sign_digit // self.BASE)
            self.digits[pos] = c * (sign_digit % self.BASE)
        elif abs(self.digits[digit_length - 1]) >= self.BASE:
            self.digits = self.digits + [c * (c * self.digits[digit_length - 1] // self.BASE)]
            self.digits[digit_length - 1] = c * (c * self.digits[digit_length - 1] % self.BASE)

    def __add__(self, other):
        s = reversed([
            a + b
            for a, b in zip_longest(
                self.digits,
                other.digits,
                fillvalue=0
            )])
        ret = LongNumber(list(s))
        ret.normalize()
        return ret

    def __sub__(self, other):
        if self == other:
            return LongNumber('0')
        subtract = cp.copy(other)
        subtract.negate()
        return self + subtract

    def __mul__(self, other):
        a, b = self.digits, other.digits
        ret = LongNumber('0')
        for i in range(len(a)):
            term = [0] * i + [a[i] * j for j in b]
            term.reverse()
            to_add = LongNumber(term)
            to_add.normalize()
            ret += to_add
        ret.normalize()
        return ret

    def __lt__(self, other):
        status = False
        for a, b in zip_longest(
                self.digits,
                other.digits,
                fillvalue=0
        ):
            if a < b:
                status = True
            if a > b:
                status = False
        return status

    def __eq__(self, other):
        if not len(self.digits) == len(other.digits):
            return False
        a, b = self.digits, other.digits
        for i in range(len(a)):
            if not a[i] == b[i]:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return not self > other

    def __floordiv__(self, other):
        if other == zero:
            return None
        if self == zero:
            return LongNumber('0')

        res, m = self.column_divide(self, other)

        if self.is_negative() != other.is_negative():
            if res == zero:
                res = LongNumber('0')
            else:
                res *= minus_one
                res -= one

        return res

    # 987654
    # 123
    def column_divide(self, a, b):
        res = LongNumber('0')
        w = cp.deepcopy(a)
        q = cp.deepcopy(b)
        if w < zero:
            abs_a = w.abs()
        else:
            abs_a = w

        if q < zero:
            abs_b = q.abs()
        else:
            abs_b = q

        first_step = True
        x = LongNumber('0')

        if abs_a < abs_b:
            return LongNumber('0'), a
        while len(abs_a.digits) > 0:
            x = x * long_base + LongNumber(abs_a.digits[len(abs_a.digits) - 1])

            abs_a.digits.pop()
            result_digit = LongNumber('0')

            while x <= abs_b:
                if len(abs_a.digits) > 0:
                    if not first_step:
                        res = res * long_base

                    x = x * long_base + LongNumber(abs_a.digits[len(abs_a.digits) - 1])

                    abs_a.digits.pop()
                else:
                    break

            while x >= abs_b:
                result_digit += one
                x -= abs_b

            first_step = False
            res = res * long_base + LongNumber(result_digit)
        return res, x

    def __mod__(self, other):
        if other == zero:
            raise Exception()
        return self - (self // other) * other

    def __pow__(self, exponent):
        if exponent == zero:
            return LongNumber('1')
        b = cp.copy(self)

        res = LongNumber('1')
        while exponent > zero:
            if exponent % two == one:
                res = res * b
            exponent //= two
            b = b * b
        return res


    def sqrt(self):
        """Heron`s algo implementation for square root"""
        x = self
        if self == zero:
            return LongNumber('0')
        precise_enough = False
        while not precise_enough:
            old_x = x
            x = (x + self // x) // two
            if (old_x - x) <= one:
                precise_enough = True
        return x

    @staticmethod
    def GCD(n1, n2):
        while min(n1, n2) > zero:
            if n1 >= n2:
                n1 %= n2
                continue
            if n2 > n1:
                n2 %= n1
                continue
        return max(n1, n2)

    @staticmethod
    def GCD_n(*args):
        res = args[0]
        for a in args:
            res = LongNumber.GCD(res, a)
        return res

    @staticmethod
    def add_mod(a, b, m):
        return (a + b) % m

    @staticmethod
    def sub_mod(a, b, m):
        return (a - b) % m

    @staticmethod
    def pow_mod(B, E, M):
        b = cp.deepcopy(B)
        e = cp.deepcopy(E)
        m = cp.deepcopy(M)

        res = LongNumber('1')
        b %= m
        if b == zero:
            return 0

        while e > zero:
            if e % two == one:
                res = (res * b) % m
            e //= two
            b = (b * b) % m
        return res

    @staticmethod
    def mult_mod(a, b, m):
        return (a * b) % m

    @staticmethod
    def div_mod(a, b, m):
        return (a // b) % m

    def __hash__(self):
        return hash(self.__str__())


zero = LongNumber('0')
one = LongNumber('1')
minus_one = LongNumber('-1')
two = LongNumber('2')
long_base = LongNumber('10')
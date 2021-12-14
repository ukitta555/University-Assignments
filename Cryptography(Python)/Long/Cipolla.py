from LegandreJacobi import legendre_symbol
from LongNumber import LongNumber

zero = LongNumber('0')
one = LongNumber('1')
minus_one = LongNumber('-1')
two = LongNumber('2')

def cipolla(n, p):
    is_square = legendre_symbol(n, p) == one
    if is_square:
        selected_a = None
        a_squared_minus_n = None
        for a in range(2, 10):
            a_squared_minus_n = (LongNumber(a) * LongNumber(a) - n)
            while a_squared_minus_n < zero:
                a_squared_minus_n += p

            print("A^2 - N", a_squared_minus_n)
            if legendre_symbol(a_squared_minus_n, n) == minus_one:
                selected_a = LongNumber(a)
                break
        print("Selected A:", selected_a.__str__())
        print ("SQRT:", a_squared_minus_n.sqrt())

        u, v = selected_a, LongNumber(1)
        x, y = LongNumber(1), LongNumber(0)
        power = (p + one) // two
        while power > zero:
            if power % two == one:
                x, y = (x * u + y * v * a_squared_minus_n) % p, (x * v + y * u) % p
            u, v = (u * u + v * v * a_squared_minus_n) % p, two * u * v % p
            power //= two

        assert y == zero
        return x
    return None

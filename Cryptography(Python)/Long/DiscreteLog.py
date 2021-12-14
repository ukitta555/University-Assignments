"""
This is a simple, yet straight forward implementation of Pollard's rho algorithm for discrete logarithms
It computes X such that G^X = H mod P.
p must be a safe prime, such that there is a prime q for which p = 2q+1 holds true.
"""
from LongNumber import LongNumber

two = LongNumber(2)
one = LongNumber(1)
zero = LongNumber(0)


def ext_euclid(a, b):
    """
    Extended Euclidean Algorithm
    :param a:
    :param b:
    :return:
    """
    if b == zero:
        return a, LongNumber('1'), LongNumber('0')
    else:
        d, xx, yy = ext_euclid(b, a % b)
        x = yy
        y = xx - (a // b) * yy
        return d, x, y


def inverse(a, n):
    """
    Inverse of a in mod n
    :param a:
    :param n:
    :return:
    """
    return ext_euclid(a, n)[1]


def xab(x, a, b, G, H, P, Q):
    """
    Pollard Step
    :param x:
    :param a:
    :param b:
    :return:
    """
    sub = x % LongNumber('3') # Subsets

    if sub == zero:
        x = x*G % P
        a = (a+one) % Q

    if sub == one:
        x = x * H % P
        b = (b + one) % Q

    if sub == two:
        x = x*x % P
        a = a*two % Q
        b = b*two % Q

    return x, a, b


def pollard_discrete(G, H, P):

    # P: prime
    # H:
    # G: generator
    Q = (P - LongNumber(1)) // LongNumber(2)  # sub group


    x = G*H
    a = LongNumber('1')
    b = LongNumber('1')

    X = x
    A = a
    B = b

    while True:
        # Tortoise
        x, a, b = xab(x, a, b, G, H, P, Q)

        # Hare
        X, A, B = xab(X, A, B, G, H, P, Q)
        X, A, B = xab(X, A, B, G, H, P, Q)

        if x == X:
            break


    nom = a-A
    denom = B-b

    res = (inverse(denom, Q) * nom) % Q

    if verify(G, H, P, res):
        return res

    return res + Q


def verify(g, h, p, x):
    """
    Verifies a given set of g, h, p and x
    :param g: Generator
    :param h:
    :param p: Prime
    :param x: Computed X
    :return:
    """
    return LongNumber.pow_mod(g, x, p) == h
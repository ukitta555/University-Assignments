import copy
from math import gcd

from LongNumber import LongNumber

zero = LongNumber('0')
one = LongNumber('1')
two = LongNumber('2')
three = LongNumber('3')
six = LongNumber('6')
nine = LongNumber('9')


def is_prime(number_in_question):
    if number_in_question == two or number_in_question == three:
        return True
    if number_in_question < two or number_in_question % two == zero:
        return False
    if number_in_question < nine:
        return True
    if number_in_question % three == zero:
        return False
    r = number_in_question.sqrt()
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = LongNumber('5')
    while f <= r:
        if number_in_question % f == zero or number_in_question % (f + two) == zero:
            return False
        f += six
    return True


def pollard_rho(N, seed=LongNumber('1'), f=lambda x: x ** two + one):
    n = copy.deepcopy(N)
    if n == one:
        return []
    elif is_prime(n):
        return [n]

    factors = []

    while True:
        x, y, d = seed, seed, LongNumber('1')
        attempts = 10000
        while d == one or d == n:
            x = f(x) % n
            y = f(f(y) % n) % n
            d = LongNumber.GCD((x - y).abs(), n)  # equivalent to comparison f_i(x0) = f_j(x0) (mod p),
            # where p is a factor
            attempts -= 1
            if not attempts:
                return factors + [n]

        n //= d

        factors_of_factor = pollard_rho(d)

        if len(factors_of_factor) == 1:
            print(f"Couldn't factorize {factors_of_factor[0].__str__()} further (prime or not enough attempts given)")

        for factor in factors_of_factor:
            factors.append(factor)

        if is_prime(n):
            print ("Is prime!")
            factors.append(n)
            break

    return factors

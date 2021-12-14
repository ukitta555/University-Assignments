import random

from LegandreJacobi import legendre_symbol, jacobi_symbol
from LongNumber import LongNumber

zero = LongNumber('0')
one = LongNumber('1')
two = LongNumber('2')
three = LongNumber('3')
six = LongNumber('6')
eight = LongNumber('8')
nine = LongNumber('9')
minus_one = LongNumber('-1')
N = LongNumber('10')


def solovei_strassen(a):
    i = N
    while i > zero:
        k = LongNumber(random.randrange(int(a.__str__())))
        print("Random number is", k.__str__())
        if LongNumber.GCD(a, k) > one:
            print ("GCD isn't one")
            return False
        jacobi = jacobi_symbol(k, a)

        while jacobi < zero:
            jacobi += a

        if LongNumber.pow_mod(k, (a - one) // two, a) != jacobi % a:
            print ("Mod comparison failed:", LongNumber.pow_mod(k, (a - one) // two, a), jacobi % a)
            return False
        i -= one
    return True

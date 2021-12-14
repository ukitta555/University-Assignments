import copy

from LongNumber import LongNumber
from RhoPollard import pollard_rho

'''
1.  Если число a отрицательно, то выделяем множитель L(-1, p);
2.  Заменяем число a на остаток от деления числа a на p;
3.  Раскладываем число a в произведение в простых сомножителей 
a = a1^α1 * a2^α2 ... ak^αk;
если число на простые множители не разлагается, то переходим на щаг 
4.  Переходим к разложению 
L(a, p) = L(a1, p)^α1... L(ak, p)αk;
5.  Отбрасываем множители с четным значением показателя 
6.  Вычисляем символ Лежандра 
L(aj, p)^αj для aj = 2;
7.  Если все символы Лежандра в выражении 
L(a, p) = L(a1, p)^α1... L(a_k, p)α_k 
вычислены, то алгоритм вычисления L(a, p) завершаем. 
В противном случае для множителей L(a_j, p)α_j, у которых  a_j ≠ 2, применяем закон взаимности 
L(p, q) = -1^[(p-1)/2][(q-1)/2] L(q, p).
Здесь полагается, что  p = aj 
8. Переходим к шагу 1.


'''

zero = LongNumber('0')
one = LongNumber('1')
two = LongNumber('2')
three = LongNumber('3')
six = LongNumber('6')
eight = LongNumber('8')
nine = LongNumber('9')
minus_one = LongNumber('-1')


def legendre_symbol(A, P):
    a = copy.deepcopy(A)
    p = copy.deepcopy(P)
    factors = []
    if a == one:
        return a
    if a == minus_one:
        return minus_one ** ((p - one) // two)
    if a < zero:
        factors.append(LongNumber('-1'))
        a = a * LongNumber('-1')
    a %= p
    factors += pollard_rho(a)
    factor_powers = {}
    for factor in factors:
        if factor_powers.get(factor):
            factor_powers[factor] += one
        else:
            factor_powers[factor] = LongNumber('1')


    odd_factor_powers = {}
    for key, value in factor_powers.items():
        if value % two != zero:
            odd_factor_powers[key] = value

    result = LongNumber('1')
    two_factor_amount = odd_factor_powers.get(two)
    if two_factor_amount:
        power_result = minus_one ** ((p ** two - one) // eight)
        i = LongNumber('0')
        while i < two_factor_amount:
            result *= power_result
            i += one
        odd_factor_powers.pop(two)

    for key, value in odd_factor_powers.items():
        assert value % two == one
        i = LongNumber('0')
        power_result = minus_one ** (((key - one) // two) * ((p - one) // two))
        legendre = legendre_symbol(p, key)
        while i < value:
            i += one
            result *= power_result * legendre

    return result


def jacobi_symbol(a, m):
    factors = pollard_rho(m)
    result = LongNumber('1')
    if not factors:
        factors = [m]
    print(factors)
    for factor in factors:
        legendre = legendre_symbol(a, factor)
        # print ("Legendre result:", legendre, "for", a, factor)
        result *= legendre
    return result

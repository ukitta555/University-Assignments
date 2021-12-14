import time

from Cipolla import cipolla
from ElGamal import ElGamal
from EulerMobius import mobius_mu_function, euler_phi_function
from LegandreJacobi import legendre_symbol, jacobi_symbol
from LongComparison import LongComparison
from LongNumber import LongNumber
from Point import P
from SoloveiStrassen import solovei_strassen
from SystemLongComparison import SystemLongComparison
from RhoPollard import pollard_rho
from DiscreteLog import pollard_discrete, verify


def time_execution(func, *args):
    start = time.time()
    print(func(*args))
    end = time.time()
    print("Time elapsed:", end - start)


# q1 = LongNumber('-77')
# q2 = LongNumber('-24')
# f1 = LongNumber('111119')
# f2 = LongNumber('-999991')
#
# print (f1 + f2)
# print(q1 // q2)
# print(q1 % q2)
#
#
#
#
# a1 = LongNumber('13')
# b1 = LongNumber('7')
# m1 = LongNumber('24')
#
# a2 = LongNumber('8')
# b2 = LongNumber('5')
# m2 = LongNumber('75')
#
# print('Timing div mod')
# time_execution(LongNumber.div_mod, LongNumber(
#     123123123123123123123123123123123123123123123123123123123123), m2, m1)
#
#
# c1 = LongComparison(a1, b1, m1)
# c2 = LongComparison(a2, b2, m2)
# x, y = c1.solve()
# q, w = c2.solve()
# print(x, y)
# print(q, w)
#
# s = SystemLongComparison([c1,c2])
# answer = s.solve()
# print(answer[0])
# print(answer[1])
#
# # 199249
# # Time elapsed: 87.2929470539093 sec
#
# print('Timing pow mod')
# time_execution(LongNumber.pow_mod, LongNumber(547457), LongNumber(54764), LongNumber(344537))
#
# print (LongNumber.pow_mod(m1, m2, LongNumber(
#     123123123123123123123123123123123123123123123123123123123123)))
#
# a3 = LongNumber('1')
# b3 = LongNumber('2')
# m3 = LongNumber('3')
#
# a4 = LongNumber('1')
# b4 = LongNumber('3')
# m4 = LongNumber('5')
#
# a5 = LongNumber('1')
# b5 = LongNumber('1')
# m5 = LongNumber('7')
#
# c3 = LongComparison(a3, b3, m3)
# c4 = LongComparison(a4, b4, m4)
# c5 = LongComparison(a5, b5, m5)
#
# s1 = SystemLongComparison([c3, c4, c5])
#
# answer = s1.solve()
# print (answer[0], answer[1])


########################

# LAB 2

print("Rho-Pollard Factorization: \n")
print("Result:", [i.__str__() for i in pollard_rho(LongNumber(87619876495133))])
print("-----------------------")
#
# print("Rho-Pollard Discrete Logarithm: \n")
# g = LongNumber(11)
# h = LongNumber(13)
# p = LongNumber(127)

# print("Result:", pollard_discrete(g, h, p))
# print("-----------------------")
# print("Result:", verify(g, h, p, LongNumber(5142)))
# print("-----------------------")

# print("Legendre symbol: \n")
# print("Result:", legendre_symbol(LongNumber(67), LongNumber(113)))
# print("Result:", legendre_symbol(LongNumber(12345), LongNumber(331)))
# print("-----------------------")
# print("Jacobi symbol: \n")
# print("Result:", jacobi_symbol(LongNumber(67), LongNumber(113)))
# print("-----------------------")

# print("Mobius function: \n")
# print("Result:", mobius_mu_function(LongNumber(87619876495133)))
# print("-----------------------")
# print("Euler function: \n")
# print("Result:", euler_phi_function(LongNumber(10)))
# print("-----------------------")

# print("Cipolla's algorithm:")
# print("Result:", cipolla(LongNumber(10), LongNumber(13)))
# print("-----------------------")
#
# print("Solovey-Strassen")
# print("Result:", solovei_strassen(LongNumber(59)))
# print("----------------------")
# print("Result:", solovei_strassen(LongNumber(60)))
# print("----------------------")

print("El-Gamal")
message = P * 1233
# Bob generates a key pair
secret_key, public_key = ElGamal.generate_key()
# Encrypt secret message
encoded_text = ElGamal.encrypt(public_key, message)
# Decrypt message
received_message = ElGamal.decrypt(secret_key, encoded_text)
# Check if correct
print(message == received_message)
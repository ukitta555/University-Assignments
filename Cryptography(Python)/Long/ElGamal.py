from random import randrange

from Point import Point, P


class ElGamal:
    @staticmethod
    def encrypt(public_key, message):
        r = randrange(1, Point.p)   # get random number from group
        d = public_key * r
        g = r * P
        h = message + d
        return g, h

    @staticmethod
    def decrypt(secret_key, ciphertext) -> Point:
        g, h = ciphertext
        secret = g * secret_key
        message = h - secret
        return message

    @staticmethod
    def generate_key():
        secret_key = randrange(1, Point.p)  # get random number from group (Bob's secret key)
        public_key = P * secret_key   # multiply starting point by this number (Bob's public key)
        return secret_key, public_key

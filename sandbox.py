"""https://projecteuler.net/problem=381

Some algebra indicates that S(p) = 8 * (-24)^-1 (mod p)
"""


import sympy
from math import factorial as f

s = 0
primes = sympy.primerange(5, 10 ** 8)
for p in primes:
    s += (8 * pow(-24, p-2, p)) % p
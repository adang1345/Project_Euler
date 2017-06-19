"""https://projecteuler.net/problem=381

Some algebra indicates that S(p) = 9 * (-24)^-1 (mod p).
The inverse of a number n mod prime p is n^(p-2) (mod p).
"""


import sympy

s = 0
primes = sympy.primerange(5, 10 ** 8)
for p in primes:
    s += (9 * pow(-24, p-2, p)) % p
print(s)

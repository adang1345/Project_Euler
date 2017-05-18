"""https://projecteuler.net/problem=132

p is a prime factor of R(10^9) iff 10^10^9 (mod 9p) = 1."""

import sympy


def modexp(a, b, n):
    """Return a^b mod n
    Function copied from http://eli.thegreenplace.net/2009/03/28/efficient-modular-exponentiation-algorithms"""
    r = 1
    while True:
        if b % 2 == 1:
            r = r * a % n
        b //= 2
        if b == 0:
            break
        a = a * a % n
    return r


b = 10**9
primes = sympy.primerange(2, 200000)
facts = []
for p in primes:
    if modexp(10, b, 9*p) == 1:
        facts.append(p)
    if len(facts) == 40:
        break

print(sum(facts))

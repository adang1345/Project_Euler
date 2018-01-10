"""https://projecteuler.net/problem=549

I took inspiration from https://en.wikipedia.org/wiki/Kempner_function to solve this problem."""

from math import factorial
import functools
import sympy


@functools.lru_cache(maxsize=None)
def kempner_prime(p, k):
    """Return the Kempner function applied to p^k.
    Precondition: p is a prime int, and k is an int >= 1."""
    n = p ** k
    mp = p
    while factorial(mp) % n != 0:
        mp += p
    return mp


def kempner(n):
    """Return the Kempner function applied to n.
    Precondition: n >= 2"""
    m = 0
    factors = sympy.factorint(n)
    p = max(factors)
    if n // p < p:
        return p
    for f in factors:
        m = max(m, kempner_prime(f, factors[f]))
    return m


N = 10 ** 8
s = 0
for i in range(2, N + 1):
    print(i)
    s += kempner(i)
print(s)

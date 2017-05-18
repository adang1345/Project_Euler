"""https://projecteuler.net/problem=133

A prime p is never a factor of R(10^n) iff (10^10^n mod 9p = 1) for some n. To test if (10^10^n mod 9p = 1) for some n,
iterate over n starting from 1. Terminate when the equation is satisfied or (10^10^n mod 9p) loops to a previous value.
"""

# current implementation is correct as far as I know but is too slow

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


def is_ever_factor(p):
    """Return whether p is a factor of R(10^n) for some n>=1."""
    n = 1
    prev = set()
    while True:
        mod = modexp(10, 10**n, 9*p)
        if mod == 1:  # (10^10^n mod 9p = 1), so answer is yes
            return True
        elif mod in prev:  # (10^10^n mod 9p) looped to a previous non-one value, so answer is no
            return False
        prev.add(mod)
        n += 1

primes = sympy.primerange(1, 100000)
c = 0
for p in primes:
    print(p)
    if not is_ever_factor(p):
        c += p
print(c)

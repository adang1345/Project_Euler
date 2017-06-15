"""https://projecteuler.net/problem=357

From experimentation, it looks like it is necessary for n%4=2 for n to be prime-generating."""

import sympy
import functools


@functools.lru_cache(maxsize=None)
def is_prime(n):
    return sympy.isprime(n)


def is_prime_generating(n):
    """Return whether every divisor d of n satisfies d+n/d is prime."""
    for d in sympy.divisors(n):
        if not is_prime(d + n // d):
            return False
    return True

s = 1
for n in range(2, 100_000_000, 4):
    if is_prime_generating(n):
        s += n

print(s)

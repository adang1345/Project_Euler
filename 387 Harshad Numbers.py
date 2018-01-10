"""https://projecteuler.net/problem=387"""

import functools
import euler
import sympy


def is_harshad(n):
    """Return true if n is a Harshad number, false otherwise.
    Precondition: n is an int > 0"""
    return n % euler.sum_digits(n) == 0


@functools.lru_cache(maxsize=None)
def find_harshad(d):
    """Return a list of right truncatable Harshad numbers with d digits.
    Precondition: d is an int > 0"""
    if d == 1:
        return list(range(1, 10))
    acc = []
    for x in find_harshad(d - 1):
        for a in range(10):
            n = x * 10 + a
            if is_harshad(n):
                acc.append(n)
    return acc


# find all the strong, right-truncatable Harshad numbers
MAX_DIGITS = 14
strong_harshads = []
for d in range(1, MAX_DIGITS):
    for x in find_harshad(d):
        if sympy.isprime(x // euler.sum_digits(x)):
            strong_harshads.append(x)

# sum all the strong, right truncatable Harshad primes
s = 0
for x in strong_harshads:
    for a in range(10):
        n = x * 10 + a
        if sympy.isprime(n):
            s += n
print(s)

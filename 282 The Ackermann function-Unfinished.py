"""https://projecteuler.net/problem=282

This implementation is too slow and requires too much memory."""

import functools
import sys


@functools.lru_cache(maxsize=None)
def tetration(a, b, m):
    t0 = 1
    for i in range(b):
        t1 = pow(a, t0, m)
        if t0 == t1:
            break
        t0 = t1
    return t1


@functools.lru_cache(maxsize=None)
def up_arrow(a, n, b, m):
    """Return a 'n up-arrows' b mod m."""
    if n == 0:
        return (a * b) % m
    elif n >= 1 and b == 0:
        return 1
    elif n == 1:
        return pow(a, b, m)
    elif n == 2:
        return tetration(a, b, m)
    return up_arrow(a, n-1, up_arrow(a, n, b-1, m), m)


@functools.lru_cache(maxsize=None)
def ackermann(a, m):
    """Return the Ackermann of a,a mod m."""
    if a == 1:
        return 3 % m
    elif a == 2:
        return 7 % m
    return (up_arrow(2, a-2, a+3, m) - 3) % m

sys.setrecursionlimit(10000000)
print(ackermann(6,14**4))

"""https://projecteuler.net/problem=88"""

import sympy
import functools
from euler import partitions


def prod(x):
    """Return the product of all elements of x."""
    p = 1
    for n in x:
        p *= n
    return p


@functools.lru_cache(maxsize=None)
def multiplicative_partitions(n):
    """Return a list of the multiplicative partitions of n.
    Precondition: n is an int >= 2"""
    factorization = sympy.factorint(n)
    factors = []
    for f in factorization:
        for _ in range(factorization[f]):
            factors.append(f)
    return {tuple(prod(x) for x in y) for y in partitions(factors)}


def min_prodsum(k):
    """Return the minimum product-sum number with set size k."""
    for n in range(k, 2*k+1):  # number has lower bound k and upper bound 2k
        for part in multiplicative_partitions(n):
            if n - sum(part) + len(part) == k:
                # check if this multiplicative partition with enough 1s added yields the correct set size
                return n
    assert False  # this should never be reached


mins = set()
for k in range(2, 12001):
    mins.add(min_prodsum(k))

print(sum(mins))

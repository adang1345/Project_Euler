"""https://projecteuler.net/problem=159

The current implementation is too slow."""

import sympy
import math


def prod(x):
    """Return the product of all elements of x."""
    p = 1
    for n in x:
        p *= n
    return p


def partition(collection):
    """Return the partitions of collection.
    Algorithm was copied from http://stackoverflow.com/questions/19368375/set-partitions-in-python."""
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset]  + smaller[n+1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def prime_factorize(n):
    """Return the prime factorization of n as a list of factors."""
    p = sympy.factorint(n)
    f = []
    for x in p:
        f.extend([x] * p[x])
    return f


def digit_sum(n):
    """Return the digit sum of n."""
    s = 0
    for a in range(int(math.log10(n)) + 1):
        s += (n % 10**(a+1) - n % 10**a) // 10**a
    return s


def digital_root(n):
    """Return the digital root of n."""
    while n >= 10:
        n = digit_sum(n)
    return n


def mdrs(n):
    """Return the maximum digital root sum of n."""
    multiplicative_partitions = set()
    m = 0
    for f in partition(prime_factorize(n)):
        f = sum(digital_root(prod(x)) for x in f)
        m = max(m, f)
    return m


s = 0
for n in range(2, 1000000):
    s += mdrs(n)
    # print(n)

print(s)

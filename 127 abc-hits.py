"""The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so
rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c

For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000."""

from math import gcd
import sympy


def radical(n):
    """Return the radical of n, i.e., the product of the distinct prime factors of n."""
    product = 1
    factors = sympy.factorint(n)
    for f in factors:
        product *= f
    return product


def is_abc_hit(a, b):
    """Return whether ints a, b, and a+b are an abc-hit. primes must be an ordered list containing at least all the
    primes less than or equal to a+b.
    Precondition: a < b"""
    c = a + b
    return 1 == gcd(a, b) and radicals[a]*radicals[b]*radicals[c] < c


radicals = [radical(x) for x in range(120001)]
abc_hits = []
c_max = 120000
for a in range(1, c_max // 2):
    # print(a)
    for b in range(a + 1, c_max + 1 - a):
        if is_abc_hit(a, b):
            abc_hits.append(a + b)

print(sum(abc_hits))

# This took 45 minutes to compute.

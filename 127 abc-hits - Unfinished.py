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


def prime_sieve(n):
    """Return a list of all prime numbers less than or equal to n."""
    primes = [2]
    for x in range(3, n + 1):
        if is_prime(x, primes):
            primes.append(x)
    return primes


def is_prime(p, primes):
    """Return whether p is prime. primes must be a list of all primes less than p."""
    for x in primes:
        if p % x == 0:
            return False
        if x > p ** 0.5:
            return True
    return True


def radical(n, primes):
    """Return the radical of n, i.e., the product of the distinct prime factors of n. primes must be an ordered list
    containing at least all the primes less than or equal to n."""
    product = 1
    for p in primes:
        if n % p == 0:
            product *= p
        if p > n:
            break
    return product


def is_abc_hit(a, b, primes):
    """Return whether ints a, b, and a+b are an abc-hit. primes must be an ordered list containing at least all the
    primes less than or equal to a+b.
    Precondition: a < b"""
    c = a + b
    return gcd(a, b) == gcd(a, c) == gcd(b, c) == 1 and radical(a * b * c, primes) < c


primes = prime_sieve(120000)
abc_hits = []

for a in range(1, 60000):
    for b in range(a + 1, 120001 - a):
        if is_abc_hit(a, b, primes):
            abc_hits.append(a + b)

print(sum(abc_hits))

# This will eventually give the right answer but will take about 21 days of computation.

"""Library of common functions needed in Project Euler problems."""

import functools
import math
import sympy
import os
import ast


@functools.lru_cache(maxsize=None)
def num_partitions(n):
    """Return the number of partitions of n."""
    if n == 0:
        return 1
    result = 0
    k = 1
    sign = 1
    while True:
        pent = (3*k**2 - k) // 2
        if pent > n:
            break
        result += sign * num_partitions(n - pent)
        pent += k
        if pent > n:
            break
        result += sign * num_partitions(n - pent)
        k += 1
        sign = -sign
    return result


def partitions(collection):
    """Return the partitions of collection.
    Algorithm was copied from http://stackoverflow.com/questions/19368375/set-partitions-in-python."""
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in partitions(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n+1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def multi_choose(n, k):
    """Return the multinomial coefficient n choose k, where k is a collection of nonnegative ints with sum n."""
    assert sum(k) == n, "The sum of the elements of collection must equal n."
    denom = 1
    for x in k:
        if x < 0:
            return 0
        denom *= math.factorial(x)
    return math.factorial(n) // denom


def choose(n, k):
    """Return n choose k."""
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def sum_digits(n):
    """Return the sum of the digits in n.
    Precondition: n is an int >= 0"""
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def primerange(a, b):
    """Generate a list of primes in the range [a, b). For efficiency, first check primes.txt, a file containing a list
    of all primes generated so far. Otherwise, use sympy.primerange and save new primes into primes.txt.
    Preconditions: primes.txt does not exist, or it is a newline-separated list of primes from 2 onward
                   a and b are ints"""
    assert type(a) == type(b) == int, "endpoints must be ints"
    if not os.path.isfile("primes.txt"):
        open("primes.txt", "w").close()
    file = open("primes.txt", "r+")
    p = 0
    for p in file:
        p = int(p[:-1])
        if p < a:
            continue
        if p >= b:
            file.close()
            return
        yield p
    start = p + 1
    for p in sympy.primerange(start, b):
        file.write(str(p))
        file.write("\n")
        if p >= a:
            yield p
    file.close()


def factorrange(a, b):
    """Generate the prime factorization of ints in the range [a, b). For efficiency, first check factors.txt, a file
    containing a list of all factorizations computed so far. Otherwise, use sympy.factorint and save new factorizations
    into factors.txt. A prime factorization is represented as a dictionary with primes as keys and their multiplicities
    as values.
    Preconditions: factors.txt does not exist, or it is a newline-separated list of factorizations from 1 onward
                   a and b are ints
                   a > 0"""
    assert type(a) == type(b) == int, "endpoints must be ints"
    assert a > 0, "a must be > 0"
    if not os.path.isfile("factors.txt"):
        open("factors.txt", "w").close()
    file = open("factors.txt", "r+")
    n = 1
    for f in file:
        if n < a:
            n += 1
            continue
        if n >= b:
            file.close()
            return
        n += 1
        yield ast.literal_eval(f)
    for n in range(n, b):
        f = sympy.factorint(n)
        file.write(str(f))
        file.write("\n")
        if n >= a:
            yield f
    file.close()


if __name__ == "__main__":
    n = 80_000_000
    for x in factorrange(80_000_000, 10**8):
        print(n, end=": ")
        print(x)
        n += 1

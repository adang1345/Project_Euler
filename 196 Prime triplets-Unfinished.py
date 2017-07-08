"""https://projecteuler.net/problem=196

This code passes all test cases but gives the wrong solution. I'm not sure why."""

import sympy
import functools


def row(n):
    """Return a range of integers in row n of the triangle."""
    return range((n**2-n+2)//2, n*(n+1)//2+1)


@functools.lru_cache(maxsize=64)
def isprime(n):
    """Return whether n is prime."""
    return sympy.isprime(n)


def in_prime_triple(p, n):
    """Return whether prime p in row n of the triangle is part of a prime triplet.
    Precondition: n > 2

    Let the numbers around the prime be numbered in the following way.
    1   2   3   4   5
    6   7   8   9   10
    11  x   p   x   15
    16  17  18  19  20
    21  22  23  24  25
    Positions 12 and 14 can't be prime because all primes past row 2 of the triangle are odd, so the numbers immediately
    left and right of p are even. I have marked these positions with x. This leaves 39 potential prime triplets:
    (11,7,p), (6,7,p), (1,7,p), (2,7,p), (3,7,p),
    (7,8,p), (2,8,p), (3,8,p), (4,8,p), (9,8,p),
    (3,9,p), (4,9,p), (5,9,p), (10,9,p), (15,9,p)
    (15,19,p), (20,19,p), (25,19,p), (24,19,p), (23,19,p)
    (19,18,p), (24,18,p), (23,18,p), (22,18,p), (17,18,p)
    (11,17,p), (16,17,p), (21,17,p), (22,17,p), (23,17,p)
    (7,p,17), (7,p,18), (7,p,19),
    (8,p,17), (8,p,18), (8,p,19),
    (9,p,17), (9,p,18), (9,p,19)
    """
    i = row(n).index(p)
    assert isprime(p)
    try:  # (11, 7, p)
        if i >= 2 and isprime(row(n)[i-2]) and isprime(row(n-1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (6, 7, p)
        if i >= 2 and isprime(row(n-1)[i-2]) and isprime(row(n-1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (1, 7, p)
        if i >= 2 and isprime(row(n-2)[i-2]) and isprime(row(n-1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (2, 7, p)
        if i >= 1 and isprime(row(n-2)[i-1]) and isprime(row(n-1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (3, 7, p)
        if i >= 1 and isprime(row(n-2)[i]) and isprime(row(n-1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (7, 8, p)
        if i >= 1 and isprime(row(n-1)[i-1]) and isprime(row(n-1)[i]):
            return True
    except IndexError:
        pass
    try:  # (2, 8, p)
        if i >= 1 and isprime(row(n-2)[i-1]) and isprime(row(n-1)[i]):
            return True
    except IndexError:
        pass
    try:  # (3, 8, p)
        if isprime(row(n-2)[i]) and isprime(row(n-1)[i]):
            return True
    except IndexError:
        pass
    try:  # (4, 8, p)
        if isprime(row(n-2)[i+1]) and isprime(row(n-1)[i]):
            return True
    except IndexError:
        pass
    try:  # (9, 8, p)
        if isprime(row(n-1)[i+1]) and isprime(row(n-1)[i]):
            return True
    except IndexError:
        pass
    try:  # (3, 9, p)
        if isprime(row(n-2)[i]) and isprime(row(n-1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (4, 9, p)
        if isprime(row(n-2)[i+1]) and isprime(row(n-1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (5, 9, p)
        if isprime(row(n-2)[i+2]) and isprime(row(n-1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (10, 9, p)
        if isprime(row(n-1)[i+2]) and isprime(row(n-1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (15, 9, p)
        if isprime(row(n)[i+2]) and isprime(row(n-1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (15, 19, p)
        if isprime(row(n)[i+2]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
            pass
    try:  # (20, 19, p)
        if isprime(row(n+1)[i+2]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
            pass
    try:  # (25, 19, p)
        if isprime(row(n+2)[i+2]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
            pass
    try:  # (24, 19, p)
        if isprime(row(n+2)[i+1]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
            pass
    try:  # (23, 19, p)
        if isprime(row(n+2)[i]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
            pass
    try:  # (19, 18, p)
        if isprime(row(n+1)[i+1]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (24, 18, p)
        if isprime(row(n+2)[i+1]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (23, 18, p)
        if isprime(row(n+2)[i]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (22, 18, p)
        if i >= 1 and isprime(row(n+2)[i-1]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (17, 18, p)
        if i >= 1 and isprime(row(n+1)[i-1]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (11, 17, p)
        if i >= 2 and isprime(row(n)[i-2]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (16, 17, p)
        if i >= 2 and isprime(row(n+1)[i-2]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (21, 17, p)
        if i >= 2 and isprime(row(n+2)[i-2]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (22, 17, p)
        if i >= 1 and isprime(row(n+2)[i-1]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (23, 17, p)
        if i >= 1 and isprime(row(n+2)[i]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (7, p, 17)
        if i >= 1 and isprime(row(n-1)[i-1]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (7, p, 18)
        if i >= 1 and isprime(row(n-1)[i-1]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (7, p, 19)
        if i >= 1 and isprime(row(n-1)[i-1]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (8, p, 17)
        if i >= 1 and isprime(row(n-1)[i]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (8, p, 18)
        if isprime(row(n-1)[i]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (8, p, 19)
        if isprime(row(n-1)[i]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
        pass
    try:  # (9, p, 17)
        if i >= 1 and isprime(row(n-1)[i+1]) and isprime(row(n+1)[i-1]):
            return True
    except IndexError:
        pass
    try:  # (9, p, 18)
        if isprime(row(n-1)[i+1]) and isprime(row(n+1)[i]):
            return True
    except IndexError:
        pass
    try:  # (9, p, 19)
        if isprime(row(n-1)[i+1]) and isprime(row(n+1)[i+1]):
            return True
    except IndexError:
        pass
    return False


def s(n):
    """Return the sum of primes in row n that are elements of prime triplets."""
    sum_primes = 0
    for p in sympy.primerange((n**2-n+2)//2, n*(n+1)//2+1):
        if in_prime_triple(p, n):
            sum_primes += p
    return sum_primes


print(s(5678027) + s(7208785))

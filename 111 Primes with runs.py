"""https://projecteuler.net/problem=111

For each digit d, iterate through all 10-digit numbers with 9 repeats of d and sum all the primes. If no primes are
found, then iterate through all numbers with 8 repeats of d and search again for primes. If none are found, do the same
for 7 repeats, and so on."""

import itertools
import sympy


def unpack(t):
    """Given a multi-level nested tuple t of integers, unpack all levels and return a list, retaining the former order.
    If t is an integer, then return a list with just t.
    Example: unpack((1,2,(3,4),(5,6,(7,(8,)))) returns [1,2,3,4,5,6,7,8]"""
    if isinstance(t, int):
        return [t]
    unpacked = []
    for x in t:
        if isinstance(x, int):
            unpacked.append(x)
        else:
            unpacked.extend(unpack(x))
    return unpacked


def s(n, d):
    """Return S(n, d) as defined in the problem."""
    for num_d in range(n-1, 0, -1):  # iterate over number of repeats of this digit
        c = 0
        for digit_positions in itertools.combinations(range(n), num_d):
            # iterate over which positions to use as the repeated digit
            num = [None] * n
            other_positions = tuple(set(range(n)).difference(digit_positions))
            for x in digit_positions:
                num[x] = d
            other_positions_iterator = range(10)
            for _ in range(len(other_positions)-1):
                other_positions_iterator = itertools.product(other_positions_iterator, range(10))
            for x in other_positions_iterator:
                x = unpack(x)
                for i in range(len(x)):
                    num[other_positions[i]] = x[i]
                if num[0] == 0:  # ignore numbers with initial digit 0
                    continue
                num_int = int("".join(map(str, num)))
                if sympy.isprime(num_int):
                    c += num_int
        if c > 0:
            return c

su = 0
for d in range(10):
    su += s(10, d)
print(su)

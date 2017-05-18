"""https://projecteuler.net/problem=204"""

import sympy
import math


def nmax(b):
    """Return the largest integer n for which b^n <= 10^9."""
    return int(9 * math.log(10, b))


m = 10 ** 9
primes = list(sympy.primerange(2, 100))
p = 0
prev_solutions = list(range(nmax(primes[p])+1))
while p < len(primes)-1:
    p += 1
    for s in prev_solutions:
        # TODO
        pass
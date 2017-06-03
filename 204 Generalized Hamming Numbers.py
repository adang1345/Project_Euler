"""https://projecteuler.net/problem=204"""

import sympy
import math
import time

t = time.time()


def nmax(b, m):
    """Return the largest integer n for which b^n <= m."""
    return int(math.log(m, b))


def powerp(a, b):
    """Return the product of the element-wise raising of a to the power b.
    Precondition: a and b are nonempty lists of ints with the same length"""
    assert len(a) == len(b) and len(a) > 0
    p = 1
    for x,y in zip(a, b):
        p *= x ** y
    return p


m = 10 ** 9
primes = list(sympy.primerange(2, 100))
print(primes)
p = 0
prev_solutions = [[x] for x in range(nmax(primes[p], m)+1)]
while p < len(primes)-1:
    p += 1
    solutions = []
    for s in prev_solutions:
        next_prime_range = range(nmax(primes[p], m // powerp(primes[:len(s)], s)) + 1)
        solutions.extend(s + [x] for x in next_prime_range)
        prev_solutions = solutions

print("Solution: " + str(len(solutions)))
print("Time (s): " + str(time.time() - t))

"""https://projecteuler.net/problem=130

Some code is copied from the solution to problem 129."""

import math
import sympy


def A(n):
    k = 1
    while pow(10, k, 9*n) != 1:
        k += 1
    return k


composites = [91, 259, 451, 481, 703]
n = 705
while len(composites) < 25:
    if math.gcd(n, 10) == 1 and (n-1) % A(n) == 0 and not sympy.isprime(n):
        composites.append(n)
    n += 2
print(composites)
print(f"Sum: {sum(composites)}")

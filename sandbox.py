"""https://projecteuler.net/problem=549"""

import sympy
import time


def s(n):
    factors = sympy.factorint(n)
    max_factor = max(factors)
    return max_factor * factors[max_factor]


t = time.time()
S = 0
LIMIT = 10 ** 8
for i in range(LIMIT, 1, -1):
    S += s(i)
    if i % 1000 == 0:
        print(i)
print(S)
print(time.time() - t)

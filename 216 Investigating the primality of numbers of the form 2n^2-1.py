"""https://projecteuler.net/problem=216"""

import sympy

c = 1  # start count with 1 because the filter in the loop below will
for n in range(50_000_000, 0, -1):
    if n % 7 == 2 or n % 7 == 5:  # 2n^2-1 will be divisible by 7 in this case
        continue
    if sympy.isprime(2 * n**2 - 1):
        c += 1

print(c)

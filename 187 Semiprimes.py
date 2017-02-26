"""https://projecteuler.net/problem=187"""

import sympy

n = 10 ** 8
c = 0
primes = list(sympy.sieve.primerange(2, n//2))
for x in range(len(primes)):
    y = x
    while y < len(primes) and primes[x] * primes[y] < n:
        c += 1
        y += 1

print(c)

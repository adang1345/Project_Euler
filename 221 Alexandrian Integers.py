"""https://projecteuler.net/problem=221

According to OEIS A147811, the Alexandrian integers are of the form p(p+d)(p+(p^2+1)/d), where d runs over divisors of
p^2+1 and p runs over all positive integers."""

import sympy

a = set()
for p in range(200000):
    for d in sympy.divisors(p**2 + 1):
        a.add(p*(p+d)*(p+(p**2+1)//d))

a = list(a)
a.sort()
print(a[150000])

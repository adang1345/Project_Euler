"""https://projecteuler.net/problem=133

A prime p is never a factor of R(10^n) iff (10^10^n mod 9p = 1) for some n. To test if (10^10^n mod 9p = 1) for some n,
iterate over n starting from 1. Terminate when the equation is satisfied or (10^10^n mod 9p) loops to a previous value.
This method is too slow, though, so I set a guess for the upper bound of n that will provide the correct answer for this
problem. Through trial-and-error, this upper bound can be as low as 16.
"""

import sympy


def is_ever_factor(p, nmax):
    """Return whether p is a factor of R(10^n) for some n>=1. If n reaches nmax and the answer has not been found,
    assume that p is not a factor."""
    n = 1
    prev = set()
    while n <= nmax:
        mod = pow(10, 10**n, 9*p)
        if mod == 1:  # (10^10^n mod 9p = 1), so answer is yes
            return True
        elif mod in prev:  # (10^10^n mod 9p) looped to a previous non-one value, so answer is no
            return False
        prev.add(mod)
        n += 1
    return False

nmax = 16
primes = sympy.primerange(1, 100000)
c = 0
for p in primes:
    print(p)
    if not is_ever_factor(p, nmax):
        c += p
print(c)

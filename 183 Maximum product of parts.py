"""https://projecteuler.net/problem=183"""

import math


def is_nonterminating(n):
    """Return whether the maximum product of parts of n is nonterminating."""
    num_parts = int(round(n / math.e))
    f = num_parts // math.gcd(num_parts, n)
    while f % 2 == 0:
        f //= 2
    while f % 5 == 0:
        f //= 5
    return f != 1


d = 0
for n in range(5, 10001):
    print(n, is_nonterminating(n))
    if is_nonterminating(n):
        d += n
    else:
        d -= n
print(d)

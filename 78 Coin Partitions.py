"""Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins
can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million."""

import functools


@functools.lru_cache(maxsize=None)
def partition(n):
    """Return the number of partitions of n. For large values of n, this function is slow and requires numerous
    recursive calls. Memoization is recommended to mitigate these issues."""
    if n == 0:
        return 1
    result = 0
    k = 1
    sign = 1
    while True:
        pent = (3*k**2 - k) // 2
        if pent > n:
            break
        result += sign * partition(n - pent)
        pent += k
        if pent > n:
            break
        result += sign * partition(n - pent)
        k += 1
        sign = -sign
    return result


n = 1
while partition(n) % 1000000 != 0:
    n += 1
print(n)

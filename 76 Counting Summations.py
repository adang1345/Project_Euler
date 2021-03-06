"""It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?"""

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


print(partition(100) - 1)

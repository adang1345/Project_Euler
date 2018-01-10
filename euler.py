"""Library of common functions needed in Project Euler problems."""

from functools import lru_cache
from math import factorial as fact


@lru_cache(maxsize=None)
def num_partitions(n):
    """Return the number of partitions of n."""
    if n == 0:
        return 1
    result = 0
    k = 1
    sign = 1
    while True:
        pent = (3*k**2 - k) // 2
        if pent > n:
            break
        result += sign * num_partitions(n - pent)
        pent += k
        if pent > n:
            break
        result += sign * num_partitions(n - pent)
        k += 1
        sign = -sign
    return result


def partitions(collection):
    """Return the partitions of collection.
    Algorithm was copied from http://stackoverflow.com/questions/19368375/set-partitions-in-python."""
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in partitions(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n+1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def multi_choose(n, k):
    """Return the multinomial coefficient n choose k, where k is a collection of nonnegative ints with sum n."""
    assert sum(k) == n, "The sum of the elements of collection must equal n."
    denom = 1
    for x in k:
        if x < 0:
            return 0
        denom *= fact(x)
    return fact(n) // denom


def choose(n, k):
    """Return n choose k."""
    return fact(n) // fact(k) // fact(n - k)


def sum_digits(n):
    """Return the sum of the digits in n.
    Precondition: n is an int >= 0"""
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


if __name__ == "__main__":
    print(multi_choose(100, [1]))

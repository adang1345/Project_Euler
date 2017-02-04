"""The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so
rad(504) = 2 × 3 × 7 = 42.

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000)."""


def prod(factors):
    p = 1
    for x in factors:
        p *= x
    return p


def isprime(num):
    """Determine whether num is prime."""
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def primefactors(num):
    """Return set containing prime factors of num."""
    factors = [num]
    while not isprime(factors[-1]):
        for y in range(2, int(factors[-1] ** 0.5) + 1):
            if num % y == 0 and isprime(y):
                del factors[-1]
                factors.append(y)
                leftover = num // y
                factors.append(leftover)
                num = leftover
                break
    return set(factors)


info = []
for n in range(1, 100001):
    info.append((prod(primefactors(n)), n))

info.sort()
print(info[9999])

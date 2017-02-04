"""Euler's Totient function, phi(n), is used to determine the number of positive numbers less than or equal to n which
are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine,
phi(9)=6. The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which phi(n) is a permutation of n and the ratio n/φ(n) produces a minimum."""


def is_prime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def prime_factors(num):
    """Return list containing prime factorization of num. Prime factors are listed from lowest to highest.

    Begin with a list containing only num. While the last element of this list is not prime, find the smallest prime
    number that divides into the last element. Replace that last element with its smallest prime divisor and its
    cofactor. The cofactor is the former last element divided by its smallest prime factor."""
    factors = [num]
    while not is_prime(factors[-1]):
        for y in range(2, int(factors[-1] ** 0.5) + 1):
            if num % y == 0 and is_prime(y):
                del factors[-1]
                factors.append(y)
                leftover = num // y
                factors.append(leftover)
                num = leftover
                break
    return factors


def prime_factors_grouped(num):
    """Return a list of lists containing the prime factorization of num. Same factors are grouped in a sublist."""
    a = prime_factors(num)
    b = [[a[0]]]
    for x in range(1, len(a)):
        if a[x] == a[x-1]:
            b[-1].append(a[x])
        else:
            b.append([a[x]])
    return b


def phi(n):
    """Return the totient of n. Efficiency is achieved through the following two facts about the totient function.

    phi(m*n) = phi(m) * phi(n) if gcd(m,n) = 1
    phi(p^k) = p^k - p^(k-1) for prime p"""
    if n == 1:
        return 1
    a = []
    factors = prime_factors_grouped(n)
    for x in factors:
        p = x[0]
        k = len(x)
        a.append(p ** k - p ** (k-1))
    product = 1
    for x in a:
        product *= x
    return product


def are_permutations(a, b):
    """Return True if ints a and b are permutations of the same digits."""
    d1 = list(str(a))
    d2 = list(str(b))
    d1.sort()
    d2.sort()
    return d1 == d2


# find all integers x in 1..10^7 for which phi(x) and x are permutations of the same digits
candidates = []
for x in range(2, 10000000):
    ph = phi(x)
    if are_permutations(ph, x):
        candidates.append((x / ph, x))

# select the answer out of the candidates
minimum = candidates[0][0]
answer = candidates[0][1]
for x in range(1, len(candidates)):
    if candidates[x][0] < minimum:
        minimum = candidates[x][0]
        answer = candidates[x][1]

print(answer)

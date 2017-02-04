"""Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

n   Relatively Prime	φ(n)	n/φ(n)
2   1	                1	    2
3	1,2                 2	    1.5
4	1,3                 2	    2
5	1,2,3,4             4	    1.25
6	1,5                 2       3
7	1,2,3,4,5,6         6	    1.1666...
8	1,3,5,7             4       2
9	1,2,4,5,7,8         6       1.5
10	1,3,7,9             4       2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum."""


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


maximum = 2
answer = 2
for x in range(3, 1000001):
    candidate = x / phi(x)
    if candidate > maximum:
        maximum = candidate
        answer = x

print(answer)

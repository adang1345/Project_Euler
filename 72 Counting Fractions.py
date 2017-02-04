"""Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction. If we list the set of reduced proper fractions for d ? 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set. How many elements would be contained in the set of reduced proper
fractions for d <= 1,000,000?"""

# I realized that the number of reduced proper fractions with denominator d is phi(d).


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


s = 0
for d in range(2, 1000001):
    s += phi(d)

print(s)

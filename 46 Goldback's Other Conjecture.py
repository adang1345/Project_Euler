"""It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice
a square.

9 = 7 + 2*12
15 = 7 + 2*22
21 = 3 + 2*32
25 = 7 + 2*32
27 = 19 + 2*22
33 = 31 + 2*12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""


def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def prime_after(n):
    """return smallest prime greater than n"""
    n += 1
    while not isprime(n):
        n += 1
    return n

def is_twice_square(n):
    """determine if n is twice a square of an integer"""
    return int((n // 2) ** 0.5) ** 2 * 2 == n


def satisfies_conjecture(n):
    """determine whether n satisfies Goldback's other conjecture"""
    while prime_after(primes[-1]) < n:
        primes.append(prime_after(primes[-1]))
    for x in primes:
        if is_twice_square(n - x):
            return True
    return False


def next_odd_composite(n):
    """Return smallest odd composite number > n. Assume n is odd int >= 1."""
    n += 2
    while isprime(n):
        n += 2
    return n


a = 9
primes = [2]
while satisfies_conjecture(a):
    a = next_odd_composite(a)
print(a)

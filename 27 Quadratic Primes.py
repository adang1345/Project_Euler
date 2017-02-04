"""Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0."""


def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

max_number_of_primes = 0
ab_prod = 0

# For each a from -1000 to 1000 and for each b from -1000 to 1000, calculate the number of primes formed from
# consecutive values of n starting at n = 0. Determine the max of these numbers.
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while n**2 + a*n + b >= 2 and isprime(n**2 + a*n + b):
            n += 1
        if n > max_number_of_primes:
            max_number_of_primes = n
            ab_prod = a * b

print(ab_prod)

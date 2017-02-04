"""Computes the sum of all primes below 2 million"""

def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

# Start counter at 0. Test every number from 2 to 2 million. Add each prime to the counter.
prime_sum = 0
for x in range(2, 2000001):
    if isprime(x):
        prime_sum += x

print(prime_sum)

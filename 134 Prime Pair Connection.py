"""Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that
the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of
n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000."""

import math


def is_prime(n):
    """Determine whether n is prime."""
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def prime_pair_connector(pair):
    """Given a tuple of 2 consecutive primes pair, return the smallest number that is divisible by pair[1] and has
    the same last digits as pair[0]."""
    num_digits = int(math.log10(pair[0])) + 1
    increment = 10 ** num_digits
    candidate = pair[0] + increment
    while candidate % pair[1] != 0:
        candidate += increment
    return candidate


primes = [n for n in range(5, 1000004) if is_prime(n)]
prime_pairs = []
for x in range(len(primes)-1):
    prime_pairs.append((primes[x], primes[x+1]))

s = 0
for pair in prime_pairs:
    s += prime_pair_connector(pair)
    print(pair[0])

print("Sum of all s is", s)

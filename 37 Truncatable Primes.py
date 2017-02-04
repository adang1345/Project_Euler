"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""


def isprime(num):
    """Determine whether num is prime, given that num is int >= 1

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    if num == 1:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def all_prime(l):
    """determines whether every element of list l is prime"""
    for x in l:
        if not isprime(x):
            return False
    return True


def truncated_list(n):
    """return list containing all truncations of int n >= 10 from left or right, including n"""
    truncations = [n]
    n_str = str(n)
    for x in range(1, len(n_str)):
        truncations.append(int(n_str[x:]))
        truncations.append(int(n_str[:-x]))
    return truncations


truncatable_primes = []
candidate = 11
while len(truncatable_primes) < 11:  # there are known to be only 11 such primes
    if all_prime(truncated_list(candidate)):
        truncatable_primes.append(candidate)
    candidate += 2

print(sum(truncatable_primes))



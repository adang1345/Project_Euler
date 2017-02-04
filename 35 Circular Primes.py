"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""


def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def rotate_digits(n):
    """return list containing every rotation of digits in n"""
    n_str = str(n)
    rotations = []
    num_rotations = 0
    while num_rotations < len(n_str):
        rotations.append(int(n_str))
        n_str = n_str[1:] + n_str[0]
        num_rotations += 1
    return rotations


def all_prime(l):
    """determines whether every element of list l is prime"""
    for x in l:
        if not isprime(x):
            return False
    return True


circular_primes = []
for x in range(2, 1000000):
    if all_prime(rotate_digits(x)):
        circular_primes.append(x)

print(len(circular_primes))

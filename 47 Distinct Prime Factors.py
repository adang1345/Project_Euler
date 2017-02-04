"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?"""


def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def primefactors(num):
    """Return set containing prime factors of num.

    Begin with a list containing only num. While the last element of this list is not prime, find the smallest prime
    number that divides into the last element. Replace that last element with its smallest prime divisor and its
    cofactor. The cofactor is the former last element divided by its smallest prime factor. In the search for smallest
    prime factor of a number, it is necessary to test only the ints from 2 to the square root of the number."""

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


consecutivity = 0
n = 2
while consecutivity < 4:
    if len(primefactors(n)) == 4:
        consecutivity += 1
    else:
        consecutivity = 0
    n += 1

print(n - 4)

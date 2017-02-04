"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

from itertools import permutations


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


# make sorted list (from largest to smallest) of all pandigital numbers that might be prime
perms = list(permutations("123456789")) + list(permutations("12345678")) + list(permutations("1234567")) + \
    list(permutations("123456")) + list(permutations("12345")) + list(permutations("1234")) + \
    list(permutations("123")) + list(permutations("12"))
perms = [int("".join(a)) for a in perms if int("".join(a))%2==1]
perms.sort(reverse=True)

# test each value in list of pandigital numbers until first (and therefore largest) prime is found
for x in perms:
    if isprime(x):
        print(x)
        break

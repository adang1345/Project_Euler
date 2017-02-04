"""Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that
8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ? 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this
process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals
first falls below 10%?"""


def is_prime(num):
    """Determine whether num is prime.
    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def upper_left(n):
    """return int in upper left corner of number spiral with side length n"""
    return n ** 2 - 2 * n + 2


def upper_right(n):
    """return int in upper right corner of number spiral with side length n"""
    return n ** 2 - 3 * n + 3


def lower_right(n):
    """return int in lower right corner of number spiral with side length n"""
    return n ** 2


def lower_left(n):
    """return int in lower left corner of number spiral with side length n"""
    return n ** 2 - n + 1


diagonals = [1, 3, 5, 7, 9]
n = 5
prime_count = 3
while prime_count / len(diagonals) >= 0.1:
    new_diagonals = [upper_left(n), upper_right(n), lower_right(n), lower_left(n)]
    for x in new_diagonals:
        if is_prime(x):
            prime_count += 1
    diagonals.extend(new_diagonals)
    n += 2

print(n - 2)

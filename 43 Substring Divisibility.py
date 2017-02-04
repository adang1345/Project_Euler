"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property."""

from itertools import permutations


def is_prime_divisible(n):
    """Return true if 7 substring divisibility rules above are satisfied for n. Assume n is an integer in string
    form."""
    return int(n[1:4]) % 2 == int(n[2:5]) % 3 == int(n[3:6]) % 5 == int(n[4:7]) % 7 == int(n[5:8]) % 11 == \
        int(n[6:9]) % 13 == int(n[7:10]) % 17 == 0


# make list of all 0 to 9 pandigital numbers in string form
pandigital_numbers = ["".join(a) for a in permutations("0123456789") if a[0] != "0"]

c = 0
for x in pandigital_numbers:
    if is_prime_divisible(x):
        c += int(x)

print(c)

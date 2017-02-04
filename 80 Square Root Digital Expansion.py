"""It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal
expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots."""

from decimal import Decimal, getcontext
getcontext().prec = 100


def sum_sqrt(n):
    """Return the sum of the first 100 decimal digits of sqrt(n)."""
    s = 0
    sqrt_digits = str(Decimal(n).sqrt() % 1)
    sqrt_digits = sqrt_digits[sqrt_digits.index(".") + 1:]
    for x in sqrt_digits:
        s += int(x)
    return s


total = 0
square_numbers = [n ** 2 for n in range(1, 11)]
for x in range(2, 100):
    if x not in square_numbers:
        total += sum_sqrt(x)

print(total)

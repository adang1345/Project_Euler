"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

from math import factorial


def sum_factorial_digits(n):
    """return sum of factorials of digits in int n"""
    a = 0
    for b in str(n):
        a += factorial(int(b))
    return a


total = 0
for x in range(10, 2540161):
    if x == sum_factorial_digits(x):
        total += x

print(total)

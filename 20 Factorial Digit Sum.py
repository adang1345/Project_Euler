"""Find the sum of digits in 100!"""

from math import factorial

def sum_digits(n):
    """return sum of digits of int n"""
    c = 0
    for a in str(n):
        c += int(a)
    return c


print(sum_digits(factorial(100)))

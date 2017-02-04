"""The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.

It turns out that F(541), which contains 113 digits, is the first Fibonacci number for which the last nine digits are
1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F(2749), which contains 575 digits, is
the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that F(k) is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9
pandigital, find k."""


def is_pandigital(n):
    """Return True if n is 1-9 pandigital, False otherwise. Assume n is a string representation of an integer."""
    if len(n) != 9:
        return False
    for x in "123456789":
        if n.count(x) != 1:
            return False
    return True


fib1 = 1
fib2 = 1
fib3 = 2
k = 3
while not is_pandigital(str(fib3 % 10 ** 9)) or not is_pandigital(str(fib3)[:9]):
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
    k += 1

print(k)

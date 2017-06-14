"""https://projecteuler.net/problem=303

This is too slow. Currently I have an optimization for numbers with just the digit 9, but some still take too long to
calculate."""

def has_digit_greater_than2(n):
    """Return whether n has a digit greater than 2 in base 10."""
    if n < 10:
        return n % 10 > 2
    return n % 10 > 2 or has_digit_greater_than2(n // 10)


def f(n):
    c = n
    while has_digit_greater_than2(c):
        c += n
    return c


c = 0
for n in range(1, 10001):
    if set(str(n)) == {"9"}:  # if n contains just the digit 9, do something else to improve performance
        d = len(str(n))
        c += int("1"*d + "3"*d + "5"*d + "7"*(d-1) + "8")
    else:
        c += f(n) // n
    print(n)
print(c)

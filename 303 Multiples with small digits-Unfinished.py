"""https://projecteuler.net/problem=303

This is too slow."""

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
    c += f(n) // n
    print(n)
print(c)

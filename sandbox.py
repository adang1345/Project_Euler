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

n = 99
d = len(str(n))
print(int("1"*d + "3"*d + "5"*d + "7"*(d-1) + "8"))
print(f(n) // n)

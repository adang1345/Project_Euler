"""Find the sum of the digits of 2^1000"""

def sum_digits(n):
    """return sum of digits of int n"""
    c = 0
    for a in str(n):
        c += int(a)
    return c


print(sum_digits(2 ** 1000))

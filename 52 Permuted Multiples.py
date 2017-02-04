"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""


def is_permuted_multiple(x):
    """Return True if 2x, 3x, 4x, 5x, and 6x are permutations of same digits. Parameter x in an int."""
    double = sorted(list(str(2 * x)))
    triple = sorted(list(str(3 * x)))
    quadruple = sorted(list(str(4 * x)))
    quintuple = sorted(list(str(5 * x)))
    sextuple = sorted(list(str(6 * x)))
    return double == triple == quadruple == quintuple == sextuple


x = 1
while not is_permuted_multiple(x):
    x += 1

print(x)

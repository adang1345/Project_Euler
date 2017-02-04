"""https://projecteuler.net/problem=108

This problem is equivalent to determining the smallest n for which the number of solutions in the positive integers for
n^2=rs and r<=s exceeds 1000."""

import sympy


def prod(a):
    """Return the product of all values in a."""
    p = 1
    for x in a:
        p *= x
    return p


def num_solutions(n):
    """Determine the number of positive integer solutions for 1/x+1/y=1/n and x<=y"""
    factors = sympy.factorint(n)
    num_factors = -(-prod([2*x+1 for x in factors.values()]) // 2)
    return num_factors


n = 4
g = 3
while g <= 1000:
    n += 1
    g = num_solutions(n)
    print(n)

print("1/x+1/y=1/n has", g, "solutions when n =", n)

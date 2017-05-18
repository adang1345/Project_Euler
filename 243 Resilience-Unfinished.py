"""https://projecteuler.net/problem=243

This implementation is too slow and possibly requires too much memory."""

from sympy.ntheory import totient
from fractions import Fraction


def resilience(d):
    """Return the resilience of a denominator d."""
    return Fraction(totient(d), d-1)


f = Fraction(15499, 94744)
d = 13

while resilience(d) >= f:
    d += 1
print(d)

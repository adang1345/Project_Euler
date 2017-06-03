"""https://projecteuler.net/problem=243

From experimentation, it seems that we get a new minimum resilience only when d is increased by a certain step a few
times, then doubled. After the doubling, the step size is changed to the d before the doubling. I start with a step
size of 30 and denominator of 30. Then I keep increasing the denominator by the step size until I reach a denominator
that does not have the minimum resilience so far. Then I know that I should have doubled the denominator and changed the
step size to that denominator instead. So I undo the increase in step size, set a new step size, and double the
denominator."""

from sympy.ntheory import totient
from fractions import Fraction


def resilience(d):
    """Return the resilience of a denominator d."""
    return Fraction(totient(d), d-1)


f = Fraction(15499, 94744)
d = 30  # initialize denominator
step = 30  # initialize step size

min_resilience = resilience(d)
min_resilience_d = d

while True:
    d += step
    r = resilience(d)
    if r < min_resilience:
        min_resilience = r
        min_resilience_d = d
    else:
        d = (d - step) * 2
        step = d // 2
        r = resilience(d)
        assert r < min_resilience  # check that my assumption holds
        min_resilience = r
        min_resilience_d = d
    if r < f:
        break

print("The answer is " + str(d))

"""Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ? 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ? 1,000,000 in ascending order of size, find the numerator of the
fraction immediately to the left of 3/7."""

from fractions import Fraction

# make set of all fractions between 42854/99993 and 3/7 with denominators <= 1000000
fracs = set()
for den in range(1, 1000001):
    for num in range(42854 * den // 99993, 3 * den // 7 + 1):
        fracs.add(Fraction(num, den))

fracs = list(fracs)
fracs.sort()

print(fracs[fracs.index(Fraction(3, 7)) - 1])

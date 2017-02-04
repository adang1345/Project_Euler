"""It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example
where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?"""

from fractions import Fraction


def num_digits(n):
    """return number of digits in int n"""
    return len(str(n))


# Generate list containing first 1000 expansions. The (n+1)th expansion is 1+1/(1+n).
expansions = [Fraction(3, 2)]
while len(expansions) < 1000:
    expansions.append(1 + 1/(1+expansions[-1]))

c = 0
for x in expansions:
    if num_digits(x.numerator) > num_digits(x.denominator):
        c += 1

print(c)


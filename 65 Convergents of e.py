"""The sequence of partial values of continued fractions for square roots provide the best rational approximations. Let
us consider the convergents for √2.

Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e."""

from fractions import Fraction


def convergent(n, continued_frac):
    """Return the nth convergent for the continued fraction represented by continued_frac."""
    iterator = list(range(len(continued_frac[:n])))[1:-1][::-1]
    c = 0
    if n > 1:
        c = Fraction(1, continued_frac[n-1])
    for x in iterator:
        c = Fraction(1, continued_frac[x] + c)
    c += continued_frac[0]
    return c


# generate list representing continued fraction of e to the 100th term
e = [2]
for k in range(33):
    e.extend([1, 2 * (k+1), 1])

print(sum([int(x) for x in str(convergent(100, e).numerator)]))

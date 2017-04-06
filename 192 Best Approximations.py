"""https://projecteuler.net/problem=192"""

from fractions import Fraction
import math
from decimal import Decimal, getcontext


def continued_fraction(s):
    """Return the continued fraction expansion of the sqrt of n. This is expressed as a list, where n[1:] repeats
    infinitely.
    This algorithm was developed from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm.
    Precondition: s is not a perfect square."""
    m = 0
    d = 1
    a = [int(s ** 0.5)]
    while a[-1] != 2 * a[0]:
        m = d * a[-1] - m
        d = (s - m ** 2) // d
        a.append((a[0] + m) // d)
    return a


def closest(n, fracs):
    """Given integer n and list of fractions fracs, return the element of fracs that is closest to sqrt(n). This
    function may be inaccurate if the fractions are very close to each other, so ensure that Decimal.getcontext().prec
    is large enough."""
    n = Decimal(n).sqrt()
    min_index = 0
    min_diff = abs(Decimal(fracs[0].numerator) / Decimal(fracs[0].denominator) - n)
    for i in range(1, len(fracs)):
        f_value = Decimal(fracs[i].numerator) / Decimal(fracs[i].denominator)
        diff = abs(f_value - n)
        if diff < min_diff:
            min_diff = diff
            min_index = i
    # print(min_diff)
    return fracs[min_index]


def rational_approx(d, bound):
    """Return the best rational approximation for the sqrt(d) where the denominator is <= bound. This algorithm was
    written with help from https://en.wikipedia.org/wiki/Continued_fraction#Best_rational_approximations."""
    cf = continued_fraction(d)
    n = 0
    h = [0, 1, cf[0]]
    k = [1, 0, 1]
    while True:
        if n < len(cf)-1:
            n += 1
        else:
            n = 1
        k_next = cf[n] * k[-1] + k[-2]
        if k_next > bound:
            candidates = [Fraction(h[-1], k[-1])]
            for final_term in range(math.ceil(cf[n]/2), cf[n]):
                num = final_term * h[-1] + h[-2]
                denom = final_term * k[-1] + k[-2]
                if denom <= bound:
                    candidates.append(Fraction(num, denom))
            return closest(d, candidates)
        h.append(cf[n] * h[-1] + h[-2])
        k.append(k_next)

# keep a high decimal precision
getcontext().prec = 55

denom_sum = 0
squares = set(x**2 for x in range(1, 317))
for n in range(2, 100001):
    if n not in squares:
        denom_sum += rational_approx(n, 10**12).denominator
print(denom_sum)

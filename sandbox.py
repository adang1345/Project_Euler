"""https://projecteuler.net/problem=192
I initially thought that convergents from the continued fraction expansion were all of the best approximations, but
they are are actually only a subset of the best approximations. I will figure this out later."""
import fractions


def continued_fraction(s):
    """Return the continued fraction expansion of the sqrt of n. This is expressed as a list, where n[1:] repeat
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


def rational_approx(d, bound):
    """Return the best rational approximation for the sqrt(d) where the denominator is <= bound."""
    cf = continued_fraction(d)
    n = 0
    h = [0, 1, cf[0]]
    k = [1, 0, 1]
    while True:
        if n < len(cf)-1:
            n += 1
        else:
            n = 1
        # print(n)
        k_next = cf[n] * k[-1] + k[-2]
        if k_next > bound:
            break
        h.append(cf[n] * h[-1] + h[-2])
        k.append(k_next)
    return fractions.Fraction(h[-1], k[-1])

for d in range(100):
    print(rational_approx(2, d))
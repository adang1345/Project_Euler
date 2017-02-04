"""By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with
the nearest solution."""

from math import factorial


def nCr(n, r):
    """Return n choose r value from combinatorics"""
    return factorial(n) // (factorial(r) * factorial(n - r))


def number_rectangles(m, n):
    """Return the number of rectangles in an m x n grid."""
    return nCr(m + 1, 2) * nCr(n + 1, 2)


min_dist_from_2_mil = 2000000
for m in range(1, 200):
    for n in range(m, 200):
        num_rectangles = number_rectangles(m, n)
        if abs(2000000 - num_rectangles) < min_dist_from_2_mil:
            min_dist_from_2_mil = abs(num_rectangles - 2000000)
            area = m * n

print("The rectangle with area %s is %s away from 2 million." % (str(area), str(min_dist_from_2_mil)))

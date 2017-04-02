"""Test code snippets separately before incorporation into solutions."""

from cmath import pi, sqrt, log


def area_frac(n):
    """Compute the fraction of the L-section that is below the line given n circles in the diagram.
    I used WolframAlpha and integration to derive formulas for the area."""
    total_area = 1 - pi / 4
    area_under_line = n*(n-sqrt(2*n)+1)**2 / (2*(n**2+1)**2)
    x_i = n*(n-sqrt(2*n)+1) / (n**2+1)
    x = 1
    circle_upper = -0.5*sqrt(2-x)*x**1.5 + x + 0.5*sqrt(x*(2-x)) + (sqrt(2-x)*log(sqrt(x-2)+sqrt(x)))/sqrt(x-2)
    x = x_i
    circle_lower = -0.5*sqrt(2-x)*x**1.5 + x + 0.5*sqrt(x*(2-x)) + (sqrt(2-x)*log(sqrt(x-2)+sqrt(x)))/sqrt(x-2)
    area_under_circle = circle_upper - circle_lower
    return ((area_under_line + area_under_circle) / total_area).real


print(area_frac(15))

"""https://projecteuler.net/problem=165"""

import itertools
import time
from fractions import Fraction


def intersection(s1, s2):
    """Return the true intersection point of 2D line segments s1 and s2 as a 2-tuple of Fractions. A true intersection
    point is a point T such that s1 and s2 intersect only at point T, and T is not an endpoint of s1 or s2. If the line
    segments have no true intersection points, then return None.
    Precondition: s1 and s2 are each 2-tuples of ints"""
    a, b, c, d, e, f, g, h = s1 + s2
    # if two segments have same slope, then then they can't have a true intersection point
    if (b-d)*(e-g) == (a-c)*(f-h):
        return None
    # solve for x- and y-coordinate of intersection point if we were dealing with lines instead of line segments
    if a != c:
        x = Fraction(a*(d*e-d*g-e*h+f*g)+b*c*(g-e)+c*e*h-c*f*g, (a-c)*(f-h)+b*(g-e)+d*(e-g))
        y = Fraction(d*(a*(f-h)+e*h-f*g)+b*(c*(h-f)-e*h+f*g), (a-c)*(f-h)+b*(g-e)+d*(e-g))
    else:
        x = Fraction(c)
        y = Fraction(c*f-c*h+e*h-f*g, e-g)
    # check if intersection is on both segments
    if (x > max(a, c) or x < min(a, c) or x > max(e, g) or x < min(e, g) or
        y > max(b, d) or y < min(b, d) or y > max(f, h) or y < min(f, h)):
        return None
    # check if intersection is an endpoint
    xy = (x, y)
    if xy == (a, b) or xy == (c, d) or xy == (e, f) or xy == (g, h):
        return None
    return x, y


st = time.time()

# Generate 5000 line segments. Each segment is represented as a tuple (a,b,c,d), where (a,b) and (c,d) are the
# endpoints.
s = 290797
segments = []
for _ in range(20000):
    s = (s * s) % 50515093
    t = s % 500
    if segments:
        if len(segments[-1]) == 4:
            segments.append((t,))
        else:
            segments[-1] += (t,)
    else:
        segments.append((t,))

true_intersection_points = set()
for segment_pair in itertools.combinations(segments, 2):
    i = intersection(*segment_pair)
    if i:
        true_intersection_points.add(i)

print("Answer: " + str(len(true_intersection_points)))
print("Time: " + str(time.time() - st))

"""It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the
almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by
no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose
perimeters do not exceed one billion (1,000,000,000)."""

import decimal
decimal.getcontext().prec = 40

def integral_area(a, b):
    """Return whether a triangle with side lengths a,a,b has an integral area."""
    area = decimal.Decimal(((2*a+b) * (2*a-b))).sqrt() * decimal.Decimal(b)/4
    return abs(area - int(area)) < 0.000000000001


p = 0
for a in range(320000000, 333333334):
    if integral_area(a, a-1):
        p += 3 + a - 1
        print(p)
    if integral_area(a, a + 1):
        p += 3 * a + 1
        print(p)

print("Total perimeter is " + str(p))
#245837857
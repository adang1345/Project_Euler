"""https://projecteuler.net/problem=139

For a tiling to occur, c must be divisible by a-b"""

import math

MAX_PERIMETER = 100000000
count = 0

# generate primitive Pythagorean triples
for m in range(2, int((MAX_PERIMETER//2)**0.5+1)):
    for n in range(1, m):
        if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
            a = 2*m*n
            b = m*m - n*n
            c = m*m + n*n
            p = a + b + c
            if c % (a-b) == 0:
                count += MAX_PERIMETER // p

print(count)

"""https://projecteuler.net/problem=139"""

import math

primitive_triples = open("139 Pythagorean.txt", "w")
MAX_PERIMETER = 100000000
for m in range(2, int((MAX_PERIMETER//2)**0.5+1)):
    for n in range(1, m):
        a = min(2*m*n, m**2-n**2)
        b = max(2*m*n, m**2-n**2)
        c = m**2+n**2
        p = a + b + c
        if math.gcd(a, b) == 1:
            primitive_triples.write(str((a, b, c)) + "\n")
    print(m)
primitive_triples.close()

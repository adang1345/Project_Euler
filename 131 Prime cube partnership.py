"""https://projecteuler.net/problem=131

With some algebra, we see that n * cuberoot(n+p) / cuberoot(n) = k. This implies that n+p and n are perfect cubes. Let
n+p=x^3 and n=y^3. Then p = x^3-y^3 = (x-y)(x^2-xy+y^2). p is prime, so either x-y=1 or x^2-xy+y^2=1. All integer
solutions to x^2-xy+y^2=1 do not satisfy x^3-y^3 being prime, so x-y=1 implies x=y+1. So p=x^3-y^3=(y+1)^3-y^3."""

import sympy

y = 1
c = 0
while True:
    p = (y+1)**3 - y**3
    if p >= 1_000_000:
        break
    if sympy.isprime(p):
        c += 1
    y += 1
print(c)

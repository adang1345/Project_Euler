"""http://projecteuler.net/problem=197"""

import math


def f(x):
    return math.floor(2**(30.403243784-x**2)) / 10**9


u = [-1]
for _ in range(500000):
    u.append(f(u[-1]))

print(u[-1] + u[-2])

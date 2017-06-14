"""https://projecteuler.net/problem=301"""

c = 0
for n in range(1, 2**30+1):
    if n ^ (2*n) ^ (3*n) == 0:
        c += 1
print(c)

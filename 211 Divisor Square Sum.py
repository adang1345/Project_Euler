import sympy
import time
import sys

t = time.time()

s = 0
for n in range(63_999_999, 0, -1):
    d2 = sum(x**2 for x in sympy.divisors(n))
    if round(d2 ** 0.5) ** 2 == d2:
        s += n
    if n % 10000 == 0:
        print(n)
        sys.stdout.flush()


print("Answer: " + str(s))
print("Time (s): " + str(time.time() - t))

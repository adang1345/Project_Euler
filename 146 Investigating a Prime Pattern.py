"""https://projecteuler.net/problem=146"""

import sympy
import time

t = time.time()

s = 0
for n in range(10, 150000000, 10):
    n2 = n ** 2
    if sympy.isprime(n2 + 1) and sympy.isprime(n2 + 3) and sympy.isprime(n2 + 7) and sympy.isprime(n2 + 9) and \
        sympy.isprime(n2 + 13) and sympy.isprime(n2 + 27) and not sympy.isprime(n2 + 5) \
            and not sympy.isprime(n2 + 11)  \
            and not sympy.isprime(n2 + 21) and not sympy.isprime(n2 + 23):
        s += n
print(str(time.time() - t) + " seconds")
print("Answer is " + str(s))

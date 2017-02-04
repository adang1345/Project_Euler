import math
import sympy


def nCr(n,r):
    """Compute n choose r.
    Precondition: n is an int >= 0. r is an int in 0..n"""
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def is_squarefree(n):
    """Determine whether n cannot be divided by a square of a prime.
    Precondition: n is an int > 1"""
    factors = sympy.factorint(n)
    prime_powers = set(factors.values())
    return prime_powers == {1}


pascal_numbers = set()
for n in range(51):
    for r in range(n // 2 + 1):
        pascal_numbers.add(nCr(n, r))

s = 1
for x in pascal_numbers:
    if is_squarefree(x):
        s += x

print(s)

"""https://projecteuler.net/problem=231"""

import sympy
import math


def factorial_factorization(n):
    """Return the prime factorization of n! This function was optimized with help from
    http://blog.janmr.com/2010/10/prime-factors-of-factorial-numbers.html"""
    primes = sympy.primerange(2, n+1)
    factorization = {}
    for p in primes:
        exp = sum(int(n / p**k) for k in range(1, int(math.log(n,p))+1))
        factorization[p] = exp
    return factorization


def subtract_factorizations(f1, f2):
    """Given prime factorizations f1 and f2 (as dictionaries), change f1 into the prime factorization of f1/f2.
    Precondition: The integer whose factorization is f1 is divisible by the integer whose factorization is f2."""
    for f in f2:
        if f1[f] == f2[f]:
            del f1[f]
        else:
            f1[f] -= f2[f]


def sum_factors(n):
    """Given n, the prime factorization of an integer, return the sum of the prime factors of that integer, allowing
    double-counting."""
    return sum(f*n[f] for f in n)


f = factorial_factorization(20000000)
subtract_factorizations(f, factorial_factorization(15000000))
subtract_factorizations(f, factorial_factorization(5000000))
print(sum_factors(f))

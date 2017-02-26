"""https://projecteuler.net/problem=137

It turns out that the nth Fibonacci golden nugget is F(n)*F(2n+1)."""


def fib(n):
    """Return the nth Fibonacci number."""
    phi = (1-5**0.5) / 2
    Phi = (1+5**0.5) / 2
    return int(round((Phi**n-phi**n) / 5**0.5))

print(fib(30) * fib(31))

"""https://projecteuler.net/problem=323

The probability of reaching 2^32-1 in n steps or fewer is (1-0.5^n)^32. So the probability of ending in exactly n steps
is (1-0.5^n)^32 - (1-0.5^(n-1)^32). The expected value of n is then Σn*P(n) as n goes from 1 to infinity."""


def p(n):
    return (1-.5**n)**32 - (1-.5**(n-1))**32


s = 0
for n in range(1, 200):
    s += n * p(n)
print(round(s, 10))

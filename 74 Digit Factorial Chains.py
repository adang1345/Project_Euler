"""The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out
that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?"""

import math


def factorial_sum(n):
    """Return the sum of the factorials of the digits of n. Assume n is a natural number."""
    digits = [int(x) for x in str(n)]
    return sum(map(math.factorial, digits))


def factorial_chain(n):
    """Return the non-repeating portion of the factorial chain of n."""
    chain = [n]
    next_element = factorial_sum(chain[-1])
    while next_element not in chain:
        chain.append(next_element)
        next_element = factorial_sum(chain[-1])
    return chain


c = 0
for x in range(1, 1000000):
    c += bool(len(factorial_chain(x)) == 60)

print(c)

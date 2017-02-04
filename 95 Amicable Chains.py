"""https://projecteuler.net/problem=95"""

import sympy


def sum_proper_divisors(n):
    """Return the sum of the proper divisors of n. Precondition: n is an int > 0"""
    prime_factors = sympy.factorint(n)
    s = 1
    for prime in prime_factors:
        exp = prime_factors[prime]
        s *= sum([prime**x for x in range(exp+1)])
    return s - n


max_chain_length = 0
max_chain = []
possibilities = set(range(1, 1000001))
while possibilities:
    chain = [possibilities.pop()]
    print(len(possibilities))
    while True:
        chain_next = sum_proper_divisors(chain[-1])
        if chain_next == 1 or chain_next == 0:
            # if chain abruptly ends, just remove current candidate
            break
        elif chain_next > 1000000:
            # if next element > 1000000, then remove all elements of this chain
            [possibilities.discard(x) for x in chain]
            break
        elif chain_next == chain[0]:
            # If chain loops back to beginning, check if new chain is the longest so far. If so, make note of this.
            # Then remove all elements of this chain from possibilities.
            if len(chain) > max_chain_length:
                max_chain_length = len(chain)
                max_chain = chain
                print(max_chain)
            [possibilities.discard(x) for x in chain]
            break
        elif chain_next in chain:
            # If chain loops back to a central number, then just remove current candidate.
            break
        else:
            chain.append(chain_next)

print(min(max_chain))

"""https://projecteuler.net/problem=214"""

import sympy


def totient_chain_length(n, arr):
    """Determine the totient chain length starting from n. arr is an array storing previously obtained totient chain
    lengths, where arr[n] is the totient chain length starting from n. If arr[n] has not previously been computed, then
    it's None. Assume that arr[1] == 1."""
    if arr[n]:
        return arr[n]
    else:
        i = 1 + totient_chain_length(sympy.totient(n), arr)
        arr[n] = i
        return i


# initialize array
arr = [None] * 40000000
arr[1] = 1

sum_p = 0
for p in sympy.primerange(2, 40000000):
    if totient_chain_length(p, arr) == 25:
        sum_p += p
print(sum_p)

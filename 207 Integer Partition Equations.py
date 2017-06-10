"""https://projecteuler.net/problem=207

Solving 4^t = 2^t + k, we get t = log2( (sqrt(4k+1) + 1) / 2 ) for integer k. The partition satisfies the restriction
that 2^t and 4^t are integers iff (sqrt(4k+1) + 1) / 2 is an integer. Setting (sqrt(4k+1) + 1) / 2 = n for some integer
n, we obtain k = n(n-1). So we need to consider only the positive integer k-values of the form n(n-1) where n>=2.

The partition is perfect iff t is an integer iff (sqrt(4k+1) + 1) / 2 is a power of 2 iff sqrt(4k+1) + 1 is a power of
2. Let sqrt(4k+1) + 1 = 2^m. Solving, we get k = 2^(2m-2) - 2^(m-1). So the perfect partitions are those where k is of
the form 2^(2m-2) - 2^(m-1) where m>=2."""

from fractions import Fraction

limit = 1 / 12345

n = 2
m = 2
perfect = 0
total = 0
while total == 0 or perfect / total >= limit:
    k = n * (n - 1)
    perfect_k = 2**(2*m-2) - 2**(m-1)
    if k == perfect_k:
        perfect += 1
        m += 1
    elif k > perfect_k:
        assert False
    total += 1
    n += 1

print(k)

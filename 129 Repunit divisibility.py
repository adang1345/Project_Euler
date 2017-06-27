"""https://projecteuler.net/problem=129

From https://en.wikipedia.org/wiki/Repunit, the formula for R(k) is R(k) = (10^k - 1)/9. To compute A(n), we want the
smallest k such that R(k) is divisible by n. Let R(k) be divisible by n. This implies

(10^k - 1)/9 is divisible by n
(10^k - 1)/9 = c*n for some c
10^k - 1 = c*(9n)
10^k = 1 (mod 9n)

So A(n) is the smallest k such that 10^k = 1 (mod 9n). A further optimization is that A(n)<n. I don't know why this is
the case."""

import math


def A(n):
    k = 1
    while pow(10, k, 9*n) != 1:
        k += 1
    return k


n = 1_000_001
m = A(n)
while m <= 1_000_000:
    n += 2
    if math.gcd(n, 10) == 1:
        m = max(m, A(n))
print(f"For n = {n}, A(n) = {m}.")

"""https://projecteuler.net/problem=173

Let n be the number of tiles used. The number of square laminae with n tiles is the number of solutions to
a^2-b^2 = n and a > b and (a+b) mod 2 = 0. Factoring, we get (a+b)(a-b) = n. Letting n = f1*f2, we get
a=(f1+f2)/2 and b=(f1-f2)/2, where f1>f2. a and b are integers, so f1 and f2 are of the same parity. a and b are of the
same parity, so f2 is even.

Therefore, f2 can be any even number in the range 2..n_max, and f1 can be any even number greater than f2+2 such that
f1*f2 <= n_max."""

n = 1000000
c = 0

for f2 in range(2, n+1, 2):
    f1 = f2 + 2
    while f1 * f2 <= n:
        f1 += 2
        c += 1
print(c)

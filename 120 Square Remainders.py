"""Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7
it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax."""


def rmax(a):
    return 2*a*((a-1) // 2)

s = 0
for a in range(3, 1001):
    s += rmax(a)

print(s)

"""https://projecteuler.net/problem=235

According to WolframAlpha, s(n) = [-3(n-300)r^(n+1) + 3(n-299)r^n - 900r + 897] / (r-1)^2. This gives
s(5000) = (-14100r^5001 + 14103r^5000 - 900r + 897) / (r-1)^2"""


def s(r):
    return (-14100*r**5001 + 14103*r**5000 - 900*r + 897) / (r-1)**2


goal = -6 * 10**11
lower_bound = 1.002
upper_bound = 1.003
r = 0
while upper_bound - lower_bound > 10**-13:
    r = (lower_bound + upper_bound) / 2
    if s(r) > goal:
        lower_bound = r
    else:
        upper_bound = r
print(round(r, 12))

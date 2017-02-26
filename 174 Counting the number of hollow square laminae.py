"""https://projecteuler.net/problem=174

This solution is built off the solution for problem 173."""

# Create a list c where c[t] is the number of ways to form a hollow square lamina from t tiles
n = 1000000
c = [None] + [0]*n

for f2 in range(2, n+1, 2):
    f1 = f2 + 2
    while f1 * f2 <= n:
        c[f1 * f2] += 1
        f1 += 2

# compute the solution from list c
nn = 0
for x in c[1:]:
    if 1 <= x <= 10:
        nn += 1
print(nn)

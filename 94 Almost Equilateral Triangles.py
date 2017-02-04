"""https://projecteuler.net/problem=94

The height of an almost equilateral triangle must be integral. Letting s = the length of a leg, h = height, we can
solve the Diophantine equations

3s^2 - 2s - 4h^2 - 1 = 0 for the case where the 3rd side is one more than the others
3s^2 + 2s - 4h^2 - 1 = 0 for the case where the 3rd side is one less than the others.

For case 1, we have fundamental solution s = 5, h = 4, and recursive solution s[n+1] = 7*s[n] + 8*h[n] - 2,
h[n+1] = 6*s[n] + 7*h[n] - 2.
For case 2, we have fundamental solution s = 17, h = 15, and recursive solution s[n+1] = 7*s[n] + 8*h[n] + 2,
h[n+1] = 6*s[n] + 7*h[n] + 2."""

# make list of (side, height) for all almost equilateral triangles with perimeter < 10^9
t = [(5, 4)]  # case 1
while True:
    s = t[-1][0]
    h = t[-1][1]
    s_next = 7 * s + 8 * h - 2
    if s_next > 333333333:
        break
    t.append((s_next, 6*s + 7*h - 2))
t2 = [(17, 15)]  # case 2
while True:
    s = t2[-1][0]
    h = t2[-1][1]
    s_next = 7 * s + 8 * h + 2
    if s_next > 333333333:
        break
    t2.append((s_next, 6*s + 7*h + 2))

print(sum([3*x[0]+1 for x in t]) + sum([3*x[0]-1 for x in t2]))

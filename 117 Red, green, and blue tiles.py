"""https://projecteuler.net/problem=117

Let r, g, and b be the number of red, green, and blue tiles, respectively. Let t be the total length of the row. Then
each whole number solution to the equation 2*r+3g+4*b <= t represents a certain combination of tiles to place. For
each solution, there are (r+g+b)!/(r!g!b!) ways to order the tiles. For each colored tile order, there are t-2*r-3*g-4*b
indistinguishable black tiles to place in r+g+b+1 urns."""

from math import factorial as fact


def balls_and_urns(b, u):
    """Return the number of ways to put b indistinguishable balls in u distinguishable urns."""
    return fact(b + u - 1) // fact(b) // fact(u - 1)


t = 50
count = 0

# compute the solutions to 2*r+3*g+4*b <= t
solutions = []
for r in range(t//2+1):
    for g in range(t//3+1):
        for b in range(t//4+1):
            if 2*r+3*g+4*b <= t:
                solutions.append((r, g, b))

# count number of tile arrangements for each solution
for s in solutions:
    r = s[0]
    g = s[1]
    b = s[2]
    count += (fact(r+g+b)//fact(r)//fact(g)//fact(b)) * balls_and_urns(t-2*r-3*g-4*b, r+g+b+1)

print(count)

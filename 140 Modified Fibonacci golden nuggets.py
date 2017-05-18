"""https://projecteuler.net/problem=140

Solving the generating function yields Ag(x) = (x + 3x^2) / (1-x-x^2). Let y = Ag(x). Then x is rational if and only if
the discriminant 5y^2+14y+1 is a square number. Solving the diophantine equation 5y^2+14y+1 = b^2 yields
b(n+1) = -9b(n) - 20y(n) - 28
y(n+1) = -4b(n) - 9y(n) - 14
According to WolframAlpha, start values are (b,y) = (7,2), (-7,2), (5,-4), (-5,-4), (2,-3), (-2,-3), (1,0), (-1,0)"""

start = [(7,2), (-7,2), (5,-4), (-5,-4), (2,-3), (-2,-3), (1,0), (-1,0)]
golden_nuggets = {x[1] for x in start if x[1] > 0}

for b,y in start:
    for _ in range(60):
        b_next = -9*b - 20*y - 28
        y_next = -4*b - 9*y - 14
        b = b_next
        y = y_next
        if y > 0:
            golden_nuggets.add(y)
golden_nuggets = list(golden_nuggets)
golden_nuggets.sort()

print(sum(golden_nuggets[:30]))
print(golden_nuggets)

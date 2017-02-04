"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ? 1000, is the number of solutions maximised?"""

# p must be a multiple of 3.


def pythagorean_triples(perimeter):
    """returns list of all Pythagorean triples corresponding to triangle with perimeter <perimeter>"""
    triples = []
    for a in range(1, perimeter//2):  # leg length must be less than 1/2 of perimeter
        for b in range(a + 1, perimeter//2):
            c = (a**2 + b**2) ** 0.5
            if abs(a + b + c - perimeter) < 1e-12:  # test if a+b+c equals perimeter, accounting for possible
                                                    # inaccuracies of float value c
                triples.append((a, b, int(c)))
    return triples


maximum_solutions = 0
p_with_maximum_solutions = 0
for p in range(3, 1000, 3):
    candidate = len(pythagorean_triples(p))
    if candidate > maximum_solutions:
        maximum_solutions = candidate
        p_with_maximum_solutions = p

print(p_with_maximum_solutions)

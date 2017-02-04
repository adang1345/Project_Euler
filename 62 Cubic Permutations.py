"""The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In
fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube."""


def are_permutations(a, b):
    """Return True if ints a and b are permutations of the same digits."""
    d1 = list(str(a))
    d2 = list(str(b))
    d1.sort()
    d2.sort()
    return d1 == d2


# make list of cubes in range 345^3..n^3
n = 10000
cubes = [n ** 3 for n in range(1, n + 1)]

for c1 in range(len(cubes)):
    for c2 in range(c1 + 1, len(cubes)):
        if are_permutations(cubes[c1], cubes[c2]):
            for c3 in range(c2 + 1, len(cubes)):
                if are_permutations(cubes[c1], cubes[c3]):
                    for c4 in range(c3 + 1, len(cubes)):
                        if are_permutations(cubes[c1], cubes[c4]):
                            for c5 in range(c4 + 1, len(cubes)):
                                if are_permutations(cubes[c1], cubes[c5]):
                                    print(cubes[c1])
                                    quit()

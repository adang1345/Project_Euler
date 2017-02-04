"""A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown
on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always
have integer length. It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer
dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is
the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99
is 1975.

Find the least value of M such that the number of solutions first exceeds one million."""


def shortest_path(x, y, z):
    """Return the type of the shortest path along the walls of a cuboid with dimensions x by y by z from one vertex
    to the opposite vertex. float is returned if the length is non-integral, and int is returned if the length is
    integral. Assume x <= y <= z."""
    min_squared_length = (x + y) ** 2 + z ** 2
    min_length = min_squared_length ** 0.5
    if int(round(min_length)) ** 2 == min_squared_length:
        return int
    else:
        return float


def number_cuboids(m):
    """Return the number of cuboids with integral side lengths up to and including m by m by m (ignoring rotations) for
    which the shortest walled path between opposite corners is integral."""
    c = 0
    for m1 in range(1, m + 1):
        for m2 in range(m1, m + 1):
            for m3 in range(m2, m + 1):
                if shortest_path(m1, m2, m3) == int:
                    c += 1
    return c


print(number_cuboids(1818))

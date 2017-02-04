"""Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a
triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above."""


def area_triangle(a, b, c):
    """Return the area of the triangle with vertices (as tuples) a, b, and c."""
    return 0.5 * ((a[0]-c[0]) * (b[1]-a[1]) - (a[0]-b[0])*(c[1]-a[1]))


def contains_origin(a, b, c):
    """Return True if triangle with vertices (as tuples) a, b, and c contains the origin, False otherwise"""
    s = 1 / (2 * area_triangle(a, b, c)) * (a[1] * c[0] - a[0] * c[1])
    t = 1 / (2 * area_triangle(a, b, c)) * (a[0] * b[1] - a[1] * b[0])
    return s > 0 and t > 0 and (1-s-t) > 0


triangle_file = open("102 Triangles.txt")
triangle_str = triangle_file.read().rstrip().replace("\n", ",")
triangle_file.close()
triangle_list = triangle_str.split(",")
triangle_coords = [(int(triangle_list[x]), int(triangle_list[x+1]))
                   for x in range(len(triangle_list)) if x % 2 == 0]


c = 0
for x in range(0, len(triangle_coords), 3):
    if contains_origin(triangle_coords[x], triangle_coords[x+1], triangle_coords[x+2]):
        c += 1

print(c)

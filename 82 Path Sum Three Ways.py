"""The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell
in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the left column to the right column."""

import networkx

with open("82 Matrix.txt") as m:
    matrix = [[int(x) for x in x.strip().split(",")] for x in m]
n = len(matrix)
g = networkx.DiGraph()

# construct nodes
g.add_node("start")
g.add_node("end")
for row in range(n):
    for col in range(n+1):
        g.add_node((row, col))

# add edges from start and to end
for row in range(n):
    g.add_edge("start", (row, 0), weight=0)
    g.add_edge((row, n), "end", weight=0)
# add edges from left to right
for row in range(n):
    for col in range(n):
        g.add_edge((row, col), (row, col+1), weight=matrix[row][col])
# add edges from top to bottom
for row in range(n-1):
    for col in range(2, n):
        g.add_edge((row, col), (row+1, col), weight=matrix[row+1][col-1])
# add edges from bottom to top
for row in range(n-1, 0, -1):
    for col in range(2, n):
        g.add_edge((row, col), (row-1, col), weight=matrix[row-1][col-1])

print(networkx.shortest_path_length(g, "start", "end", "weight"))

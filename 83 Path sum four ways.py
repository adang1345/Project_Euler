"""https://projecteuler.net/problem=83"""

import networkx

with open("83 Matrix.txt") as m:
    matrix = [[int(x) for x in x.strip().split(",")] for x in m]
n = len(matrix)
g = networkx.DiGraph()

# construct nodes
for row in range(n):
    for col in range(n+1):
        g.add_node((row, col))

# add edges from left to right and from right to left
for row in range(n):
    for col in range(n):
        g.add_edge((row, col), (row, col+1), weight=matrix[row][col])
        if col != 0:
            g.add_edge((row, col+1), (row, col), weight=matrix[row][col-1])
# add edges from top to bottom
for row in range(n-1):
    for col in range(1, n+1):
        g.add_edge((row, col), (row+1, col), weight=matrix[row+1][col-1])
# add edges from bottom to top
for row in range(n-1, 0, -1):
    for col in range(1, n+1):
        g.add_edge((row, col), (row-1, col), weight=matrix[row-1][col-1])

print(networkx.shortest_path_length(g, (0, 0), (n-1, n), "weight"))

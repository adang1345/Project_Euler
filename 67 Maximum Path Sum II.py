"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text fil
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (10^12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it. ;o)"""

# The iterative solution repeats the following process:
# - Take the second-to-last row. Replace each number with itself plus the larger of the two numbers below.
# - Remove the last row.
# Stop when only the first row remains. Now the first row contains a single number, which is the maximum path sum.

f = open("67 Triangle.txt")
triangle = [[int(y) for y in x.split()] for x in f.read().rstrip("\n").split("\n")]
f.close()

while len(triangle) > 1:
    for x in range(len(triangle[-2])):
        triangle[-2][x] += max(triangle[-1][x], triangle[-1][x+1])
    del triangle[-1]

print(triangle)

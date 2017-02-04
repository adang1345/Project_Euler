"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

# Using a quadratic regression in Excel, I found that for a box with magnitude n, corners add up to 16n^2 + 4n + 4.
# n=1 refers to the box with corners 3, 5, 7, 9. n=2 refers to the box with corners 13, 17, 21, 25.


def corner_sum(n):
    """return sum of corners of box with size n, assuming int n >= 1"""
    return 16 * n**2 + 4*n + 4

answer = sum([corner_sum(n) for n in range(1, 501)]) + 1
print(answer)

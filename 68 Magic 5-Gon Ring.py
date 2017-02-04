"""Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

[Image]

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this
example), each solution can be described uniquely. For example, the above solution can be described by the set:
4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the
maximum 16-digit string for a "magic" 5-gon ring?"""

from itertools import permutations


def check_result(p):
    """Check whether p, a tuple that is a permutation of (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), forms a magic 5-gon ring."""
    if p[1] == 10 or p[2] == 10 or p[4] == 10 or p[6] == 10 or p[8] == 10:
        return False
    if p[0] > p[3] or p[0] > p[5] or p[0] > p[7] or p[0] > p[9]:
        return False
    if p[0] + p[1] + p[2] != p[3] + p[2] + p[4]:
        return False
    if p[0] + p[1] + p[2] != p[5] + p[4] + p[6]:
        return False
    if p[0] + p[1] + p[2] != p[7] + p[6] + p[8]:
        return False
    if p[0] + p[1] + p[2] != p[9] + p[8] + p[1]:
        return False
    return True


perms = permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
m = 0
for p in perms:
    if check_result(p):
        m = max(m, int("".join([str(n) for n in [p[0], p[1], p[2], p[3], p[2], p[4], p[5], p[4], p[6], p[7], p[6], p[8],
                                                 p[9], p[8], p[1]]])))

print(m)

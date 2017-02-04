"""Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By
placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below
one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the
other cube. However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like
{0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be
impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the
extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?


For the problem, I define a "die" as a set containing six integers, each of which is in the range 0..9
"""


from itertools import combinations


def can_express_all_squares(d1, d2):
    """Given 2 dice s1 and s2, return whether the 2 dice can be used to express all square numbers under 100."""
    return ((0 in d1 and 1 in d2 or 1 in d1 and 0 in d2) and  # 01
            (0 in d1 and 4 in d2 or 4 in d1 and 0 in d2) and  # 04
            (0 in d1 and (9 in d2 or 6 in d2) or (9 in d1 or 6 in d1) and 0 in d2) and  # 09
            (1 in d1 and (6 in d2 or 9 in d2) or (6 in d1 or 9 in d1) and 1 in d2) and  # 16
            (2 in d1 and 5 in d2 or 5 in d1 and 2 in d2) and  # 25
            (3 in d1 and (6 in d2 or 9 in d2) or (6 in d1 or 9 in d1) and 3 in d2) and  # 36
            (4 in d1 and (9 in d2 or 6 in d2) or (9 in d1 or 6 in d1) and 4 in d2) and  # 49
            ((6 in d1 or 9 in d1) and 4 in d2 or 4 in d1 and (6 in d2 or 9 in d2)) and  # 64
            (8 in d1 and 1 in d2 or 1 in d1 and 8 in d2))  # 81


n = 0
all_dice = list(combinations(range(10), 6))
for d1 in range(len(all_dice)):
    for d2 in range(d1, len(all_dice)):
        if can_express_all_squares(all_dice[d1], all_dice[d2]):
            n += 1

print("Number of arrangements is " + str(n))

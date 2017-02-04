"""Compute the path from top to bottom through adjacent numbers in given triangle such that the sum of these numbers
is maximized"""

triangle = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def sum_path(path):
    """Returns the sum of the numbers on a given path of length 14 through the triangle."""
    c = 75
    previous_location = [0, 0]
    for x in range(len(path)):
        if path[x] == 0:
            current_location = [previous_location[0] + 1, previous_location[1]]
        else:
            current_location = [previous_location[0] + 1, previous_location[1] + 1]
        previous_location = current_location
        c += int(trianglenums[current_location[0]][current_location[1]])
    return c


trianglenums = [a.split() for a in triangle.split("\n")]
# Path is list of 14 numbers, each 0 or 1. 0 means move left; 1 means move right.
current_path = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
possible_answer = 0

while current_path != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
    # Treat current_path as binary number and perform binary addition of 1 at a time. This will generate every list of
    # length 14 containing 1s and 0s.
    current_path[-1] += 1
    while 2 in current_path:
        location_of_2 = current_path.index(2)
        current_path[location_of_2] = 0
        current_path[location_of_2 - 1] += 1
    possible_answer = max(possible_answer, sum_path(current_path))

print(possible_answer)

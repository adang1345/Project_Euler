"""https://projecteuler.net/problem=116"""

from math import factorial as fact


def balls_and_urns(b, u):
    """Return the number of ways to put b indistinguishable balls in u distinguishable urns."""
    return fact(b + u - 1) // fact(b) // fact(u - 1)


total_tiles = 50
count = 0

# number of red tile placements
for num_red in range(1, total_tiles//2+1):
    count += balls_and_urns(total_tiles-num_red*2, num_red+1)

# number of green tile placements
for num_green in range(1, total_tiles//3+1):
    count += balls_and_urns(total_tiles-num_green*3, num_green+1)

# number of blue tile placements
for num_blue in range(1, total_tiles//4+1):
    count += balls_and_urns(total_tiles-num_blue*4, num_blue+1)

print(count)

"""https://projecteuler.net/problem=114"""

from math import factorial as fact


def balls_and_urns(b, u):
    """Return the number of ways to put b indistinguishable balls in u distinguishable urns."""
    return fact(b + u - 1) // fact(b) // fact(u - 1)


def multi_choose(n, k):
    """Return the multinomial coefficient n choose k, where k is a list."""
    denom = 1
    for x in k:
        denom *= fact(x)
    return fact(n) // denom


def dotp(list1, list2):
    """Return the dot product of lists or ranges of integers list1 and list2."""
    assert len(list1) == len(list2)
    p = 0
    for x in range(len(list1)):
        p += list1[x] * list2[x]
    return p


t = 50
count = 0

# compute all positive integer solutions x such that sum(n*x(n), n, 3, t) <= t
prev_solutions = [[x] for x in range(t//3+1)]
for n in range(4, t+1):
    next_solutions = []
    for x in prev_solutions:
        next_solution = [x + [y] for y in range((t - dotp(x,range(3,3+len(x))))//n + 1)]
        next_solutions.extend(next_solution)
    prev_solutions = next_solutions

# enforce condition that two red blocks must be separated by at least 1 black block
solutions = []
for x in prev_solutions:
    if dotp(x, range(3,len(x)+3)) + sum(x) - 1 <= t:
        solutions.append(x)

# for each ordering of red blocks, treat the black blocks as indistinguishable balls and treat the divisions between the
# red blocks as urns, maintaining the property that two red blocks must be separated by at least 1 black block.
for x in solutions:
    num_red_blocks = sum(x)
    balls = t - dotp(x,range(3,len(x)+3)) - num_red_blocks + 1
    count += multi_choose(sum(x), x) * balls_and_urns(balls, num_red_blocks+1)

print(count)

"""https://projecteuler.net/problem=115

I took my solution to problem 114 and made some slight modifications."""

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


def fill_count(m, n):
    """Return the number of ways a row of length n can be filled with red blocks of minimum size m such that any two red
    blocks are separated by at least 1 black square."""
    count = 0

    # compute all positive integer solutions x such that sum(n*x(t), t, m, n) <= n
    prev_solutions = [[x] for x in range(n//m+1)]
    for a in range(m+1, n+1):
        next_solutions = []
        for x in prev_solutions:
            next_solution = [x + [y] for y in range((n - dotp(x,range(m,m+len(x))))//a + 1)]
            next_solutions.extend(next_solution)
        prev_solutions = next_solutions

    # enforce condition that two red blocks must be separated by at least 1 black block
    solutions = []
    for x in prev_solutions:
        if dotp(x, range(m,len(x)+m)) + sum(x) - 1 <= n:
            solutions.append(x)

    # for each ordering of red blocks, treat the black blocks as indistinguishable balls and treat the divisions between
    # the red blocks as urns.
    for x in solutions:
        num_red_blocks = sum(x)
        balls = n - dotp(x,range(m,len(x)+m)) - num_red_blocks + 1
        count += multi_choose(sum(x), x) * balls_and_urns(balls, num_red_blocks+1)
    return count


n = 160
fill_counts = [fill_count(50, n)]
while fill_counts[-1] <= 1000000:
    n += 1
    fill_counts.append(fill_count(50, n))

print("At n = " + str(n) + ", F(50, n) = " + str(fill_counts[-1]))

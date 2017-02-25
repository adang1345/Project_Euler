"""https://projecteuler.net/problem=136

I use a similar solution as for problem 135. Currently, this takes too long."""


def num_solutions1(n):
    """Determine whether the number of solutions to x^2 − y^2 − z^2 = n is 1."""
    count = 0
    for x in range(1, int(n**0.5)+1):
        cand = (x, n // x)
        if n % x == 0 and sum(cand) % 4 == 0:
            if 3*cand[0] > cand[1]:
                count += 1
                if count > 1:
                    return False
            if 3*cand[1] > cand[0] and cand[1] != cand[0]:
                count += 1
                if count > 1:
                    return False
    return count == 1


c = 0
for n in range(1, 50000000):
    if num_solutions1(n):
        c += 1
    print(n)
print("The answer is " + str(c))

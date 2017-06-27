"""https://projecteuler.net/problem=225"""


def divides_t(n):
    """Return whether n divides any number in the tribonacci sequence starting from 1,1,1."""
    t = [1, 1, 1]
    while True:
        next_t = (t[-1] + t[-2] + t[-3]) % n
        if next_t == 0:  # n does divide a number in the sequence
            return True
        t = [t[-2], t[-1], next_t]
        if t == [1, 1, 1]:  # we have cycled back to the beginning, so n doesn't divide anything
            return False


n = 1
doesnt_divide = []
while len(doesnt_divide) < 124:
    if not divides_t(n):
        doesnt_divide.append(n)
    n += 2
print(doesnt_divide[-1])

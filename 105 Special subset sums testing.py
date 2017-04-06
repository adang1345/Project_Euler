"""https://projecteuler.net/problem=105"""

from itertools import chain, combinations


def powerset(iterable):
    """Return the power set of the iterable as a generator."""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def is_special_sum_set(a):
    """Given set a, return whether it is a special sum subset."""
    b = list(powerset(a))
    c = b
    # print(list(b))
    for x in b:
        for y in c:
            if x != y:
                if sum(x) == sum(y):
                    return False
                if len(x) > len(y) and sum(x) <= sum(y):
                    return False
    return True


c = 0
for line in open("105 Sets.txt"):
    a = {int(n) for n in line.rstrip().split(",")}
    if is_special_sum_set(a):
        c += sum(a)
    print(line)
print(c)

"""https://projecteuler.net/problem=103"""

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


search_range = 4
min_sum = 1000
min_set = set()
a_set = set()
a = [19, 30, 37, 38, 39, 41, 44]  # start with a near-optimal set
for a0 in range(search_range):  # iterate each element of the set over the search range
    for a1 in range(search_range):
        for a2 in range(search_range):
            for a3 in range(search_range):
                for a4 in range(search_range):
                    for a5 in range(search_range):
                        for a6 in range(search_range):
                            a_set = {a[n] - search_range // 2 + eval("a"+str(n)) for n in range(7)}
                            if len(a_set) == 7 and sum(a_set) < min_sum and is_special_sum_set(a_set):
                                min_sum = sum(a_set)
                                min_set = a_set
                                print(min_sum, a_set)

a_list = list(a_set)
a_list.sort()
print("".join(str(n) for n in a_list))

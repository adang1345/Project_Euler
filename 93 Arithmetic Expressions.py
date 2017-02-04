"""By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic
operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n,
can be obtained, giving your answer as a string: abcd."""

from itertools import permutations


def is_pos_int(n):
    """Determine whether float/int value n is close enough to a positive integer."""
    return abs(n - int(n)) < 0.0001 and n > 0.5


def all_target_numbers(s):
    """Determine all target numbers possible using s = (a, b, c, d)"""
    target_numbers = set()
    for (a, b, c, d) in permutations(s):  # for each permutation of a,b,c,d
        a = str(a); b = str(b); c = str(c); d = str(d)
        for op1 in "+-*/":  # for each combination of 3 operations
            for op2 in "+-*/":
                for op3 in "+-*/":
                    # take care of parentheses
                    cands = set()
                    try:
                        cands.add(eval("(" + a + op1 + b + ")" + op2 + c + op3 + d))  # (a @ b) @ c @ d
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval(a + op1 + "(" + b + op2 + c + ")" + op3 + d))  # a @ (b @ c) @ d
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval(a + op1 + b + op2 + "(" + c + op3 + d + ")"))  # a @ b @ (c @ d)
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval("(" + a + op1 + b + ")" + op2 + "(" + c + op3 + d + ")"))  # (a @ b) @ (c @ d)
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval("((" + a + op1 + b + ")" + op2 + c + ")" + op3 + d))  # ((a @ b) @ c) @ d
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval("(" + a + op1 + "(" + b + op2 + c + "))" + op3 + d))  # (a @ (b @ c)) @ d
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval(a + op1 + "((" + b + op2 + c + ")" + op3 + d + ")"))  # a @ ((b @ c) @ d)
                    except ZeroDivisionError:
                        pass
                    try:
                        cands.add(eval(a + op1 + "(" + b + op2 + "(" + c + op3 + d + "))"))  # a @ (b @ (c @ d))
                    except ZeroDivisionError:
                        pass
                    int_cands = {int(x) for x in cands if is_pos_int(x)}
                    target_numbers = target_numbers.union(int_cands)
    return target_numbers


def longest_consecutive_int_length(s):
    """Given set s, return the largest n such that 1..n are all in s.
    Precondition: s is a set containing only positive integers"""
    if not s:
        return 0
    n = 1
    while n in s:
        n += 1
    return n - 1


longest_longest_length = 28
abcd = (1, 2, 3, 4)
for a in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                x = all_target_numbers((a, b, c, d))
                y = longest_consecutive_int_length(x)
                if y > longest_longest_length:
                    abcd = (a, b, c, d)
                    longest_longest_length = y
print("4 digits are " + str(abcd))
print("Longest length is " + str(longest_longest_length))

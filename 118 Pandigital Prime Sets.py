"""https://projecteuler.net/problem=118"""

import sympy
import itertools


def all_prime(s):
    """Determine whether all elements of s are prime.
    Precondition: s is a set consisting of positive ints"""
    for x in s:
        if not sympy.isprime(x):
            return False
    return True


def intify(t):
    """Given a tuple t of strings of digits, convert to integer."""
    return int("".join(t))


def partition(s):
    """Given a pandigital 9-tuple s, return all partitions with at most four 1s"""
    p1 = {intify(s)}  # 9
    p2 = {intify(s[:8]), intify(s[8])}  # 8,1
    p3 = {intify(s[:7]), intify(s[7:])}  # 7,2
    p4 = {intify(s[:7]), intify(s[7]), intify(s[8])}  # 7,1,1
    p5 = {intify(s[:6]), intify(s[6:])}  # 6,3
    p6 = {intify(s[:6]), intify(s[6:8]), intify(s[8])}  # 6,2,1
    p7 = {intify(s[:6]), intify(s[6]), intify(s[7]), intify(s[8])}  # 6,1,1,1
    p8 = {intify(s[:5]), intify(s[5:])}  # 5,4
    p9 = {intify(s[:5]), intify(s[5:8]), intify(s[8])}  # 5,3,1
    p10 = {intify(s[:5]), intify(s[5:7]), intify(s[7:])}  # 5,2,2
    p11 = {intify(s[:5]), intify(s[5:7]), intify(s[7]), intify(s[8])}  # 5,2,1,1
    p12 = {intify(s[:5]), intify(s[5]), intify(s[6]), intify(s[7]), intify(s[8])}  # 5,1,1,1,1
    p13 = {intify(s[:4]), intify(s[4:8]), intify(s[8])}  # 4,4,1
    p14 = {intify(s[:4]), intify(s[4:7]), intify(s[7:])}  # 4,3,2
    p15 = {intify(s[:4]), intify(s[4:7]), intify(s[7]), intify(s[8])}  # 4,3,1,1
    p16 = {intify(s[:4]), intify(s[4:6]), intify(s[6:8]), intify(s[8])}  # 4,2,2,1
    p17 = {intify(s[:4]), intify(s[4:6]), intify(s[6]), intify(s[7]), intify(s[8])}  # 4,2,1,1,1
    p18 = {intify(s[:3]), intify(s[3:6]), intify(s[6:])}  # 3,3,3
    p19 = {intify(s[:3]), intify(s[3:6]), intify(s[6:8]), intify(s[8])}  # 3,3,2,1
    p20 = {intify(s[:3]), intify(s[3:6]), intify(s[6]), intify(s[7]), intify(s[8])}  # 3,3,1,1,1
    p21 = {intify(s[:3]), intify(s[3:5]), intify(s[5:7]), intify(s[7:])}  # 3,3,1,1,1
    p22 = {intify(s[:3]), intify(s[3:5]), intify(s[5:7]), intify(s[7]), intify(s[8])}  # 3,2,2,1,1
    p23 = {intify(s[:3]), intify(s[3:5]), intify(s[5]), intify(s[6]), intify(s[7]), intify(s[8])}  # 3,2,1,1,1,1
    p24 = {intify(s[:2]), intify(s[2:4]), intify(s[4:6]), intify(s[6:8]), intify(s[8])}  # 2,2,2,2,1
    p25 = {intify(s[:2]), intify(s[2:4]), intify(s[4:6]), intify(s[6]), intify(s[7]), intify(s[8])}  # 2,2,2,1,1,1
    return (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13,
            p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25)

digit_strings = itertools.permutations("123456789")

sets = set()
for digit_permutation in digit_strings:
    for part in partition(digit_permutation):
        if all_prime(part):
            sets.add(frozenset(part))
print("The answer is", len(sets))

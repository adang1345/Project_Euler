"""https://projecteuler.net/problem=162

For each number of digits from 3 to 16, I first count the number of hexadecimal numbers that follow the criteria
without regard to the first digit, the subtract the number of hexadecimal numbers with a leading digit 0."""

import math


def multinomial(n, k):
    """Return the multinomial coefficient of n choose k[0]..k[len(k)-1].
    Precondition: n is an int >= 0. k is a list of ints >= 0"""
    p = 1
    for x in map(math.factorial, k):
        p *= x
    return math.factorial(n) // p


n = 0
for digits in range(3, 17):
    for num0 in range(1, digits-1):
        for num1 in range(1, digits+1 - num0):
            for numA in range(1, digits+1 - num0 - num1):
                numOther = digits - num0 - num1 - numA
                n += multinomial(digits, [num0, num1, numA, numOther]) * 13**numOther - \
                     multinomial(digits-1, [num0-1, num1, numA, numOther]) * 13**numOther

print(hex(n)[2:].upper())

"""All square roots are periodic when written as continued fractions. For conciseness, we use the notation
√23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?"""

# My first implementation took too long, so I gave up on it and commented it out.

# from decimal import Decimal, getcontext
# getcontext().prec = 1000


# def continued_fraction(n, d):
    # """Return a list of length d containing the continued fraction representation of the square root of n. The integer
    # part of the continued fraction is removed. Assume that the square root of n is irrational."""
    # n = Decimal(n).sqrt() % 1
    # f = []
    # remainder = n
    # for x in range(d):
        # int_part = int(1 / remainder)
        # remainder = (1 / remainder) % 1
        # f.append(int_part)
    # return f


# def period_length(f, max_period_length):
    # """Return the length of the period of list n, checking through a period length of max_period_length. Return 0 if
    # the period is greater than max_period_length."""
    # for guess_period_length in range(1, max_period_length + 1):
        # for i in range(len(f) // guess_period_length - 1):
            # if f[i*guess_period_length: (i+1)*guess_period_length] != \
                    # f[(i+1)*guess_period_length: (i+2)*guess_period_length]:
                # i = ""
                # break
        # if i != "":
            # return guess_period_length
    # return 0


# square_numbers = [x ** 2 for x in range(1, 101)]
# c = 0
# digit_number = 50
# max_period_length = digit_number // 2 - 1

# for x in range(1, 10001):
    # if x not in square_numbers:
        # l = period_length(continued_fraction(x, digit_number), max_period_length)
        # while l == 0:
            # digit_number += 2
            # max_period_length = digit_number // 2 - 1
            # print("Max period length is now " + str(max_period_length))
            # if max_period_length > getcontext().prec / 3:
                # getcontext().prec *= 2
            # l = period_length(continued_fraction(x, digit_number), max_period_length)
        # if l % 2 == 1:
            # c += 1
        # print(x)

# print(c)

square_numbers = [x ** 2 for x in range(1, 101)]
count = 0
for n in range(2, 10001):
    if n in square_numbers:
        continue
    limit = int(n ** 0.5)
    period = 0
    d = 1
    m = 0
    a = limit

    m = d*a - m
    d = (n - m * m) // d
    a = (limit + m) // d
    period += 1
    while a != 2 * limit:
        m = d * a - m
        d = (n - m * m) // d
        a = (limit + m) // d
        period += 1
    if period % 2 == 1:
        count += 1

print(count)

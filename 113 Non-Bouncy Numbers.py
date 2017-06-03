"""Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
for example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number;
for example, 66420. We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number;
for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below
one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?"""

from math import factorial as f


def nCr(n, r):
    return f(n) // f(r) // f(n-r)


print(nCr(110, 10) + nCr(109, 9) - 2 - 10*100)

quit()
# Below code was my original implementation. However, it takes too long.


def is_increasing(n):
    """Return whether n is an increasing number. n is represented as an integer list. For example, [1, 2] represents
    12. The first digit cannot be 0, nor can the list be empty."""
    if len(n) == 1:
        return True
    for x in range(1, len(n)):
        if n[x] < n[x-1]:
            return False
    return True


def is_decreasing(n):
    """Return whether n is a decreasing number. n is represented as an integer list. For example, [1, 2] represents
    12. The first digit cannot be 0, nor can the list be empty."""
    if len(n) == 1:
        return True
    for x in range(1, len(n)):
        if n[x] > n[x - 1]:
            return False
    return True


def next_increasing_number(n):
    """Given increasing number n, return the smallest increasing number that is greater than n. Input and ouput types
    are integer lists. Assume that n < 10^100."""
    if n[-1] != 9:  # last digit is not 9
        new_n = n[:]
        new_n[-1] += 1
    elif len(set(n)) == 1:  # every digit is 9
        new_n = [1] * (len(n) + 1)
    else:
        # find index of last digit that does not contain a 9
        i = -2
        while n[i] == 9:
            i -= 1
        index_last_digit_not9 = i + len(n)
        # construct new int list replacing everything after last digit that does not contain a 9 into that digit+1
        that_digit = n[index_last_digit_not9]
        new_n = n[:index_last_digit_not9] + [that_digit+1] * (len(n)-index_last_digit_not9)
    return new_n


def next_decreasing_number(n):
    """Given decreasing number n, return the largest decreasing number that is smaller than n. Input and output types
    are integer lists. Assume that n > 0."""
    if n == [0]:
        return False
    if n[-1] != 0:  # last digit is not 0
        new_n = n[:]
        new_n[-1] -= 1
    elif n[0] == 1 and len(set(n[1:])) == 1:  # first digit is 1 and all others are 0
        new_n = [9] * (len(n) - 1)
    else:
        # find index of last digit that does not contain a 0
        i = -2
        while n[i] == 0:
            i -= 1
        index_last_digit_not0 = i + len(n)
        # construct new int list replacing everything after last digit that does not contain a 0 into that digit-1
        that_digit = n[index_last_digit_not0]
        new_n = n[:index_last_digit_not0] + [that_digit-1] * (len(n)-index_last_digit_not0)
    return new_n

upper_limit = [9] * 100
lower_limit = [0]
c = 0

# count number of increasing numbers
n = lower_limit
while n != upper_limit:
    n = next_increasing_number(n)
    c += 1
    print(len(n))

# count number of decreasing numbers, ignoring those that are also increasing numbers
n = upper_limit
while n != lower_limit:
    n = next_decreasing_number(n)
    if len(set(n)) != 1:
        c += 1
    print(len(n))

print(c)

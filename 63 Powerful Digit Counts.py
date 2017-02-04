"""The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?"""
from math import log


def num_digits(n):
    """Return the number of digits in int n."""
    return int(round(log(n, 10), 12)) + 1


# I discovered that there exist no n-digit positive integers that are an nth power when n > 21.
max_n = 21

# make list of lists of n-digit positive integers exist which are also an nth power
l = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for n in range(2, max_n + 1):
    list_n = []
    base = 2
    while num_digits(base ** n) < n:
        base += 1
    while num_digits(base ** n) == n:
        list_n.append(base ** n)
        base += 1
    l.append(list_n)
print(l)

# print the answer
print(sum(map(len, l)))

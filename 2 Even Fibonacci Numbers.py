"""Finds the sum of all even Fibonacci numbers less than or equal to 4 million"""

# start with list containing first 3 Fibonacci numbers
fib_list = [1, 1, 2]
# start totalizer at 0
total = 0

# fib_list will always have 3 elements. While the last element is less than or equal to 4 million, test whether the
# last element is even. If so, add it to the totalizer. Then set fib_list to a subset of the Fibonacci sequence with
# a frameshift one space right.
while fib_list[2] <= 4000000:
    if fib_list[2] % 2 == 0:
        total += fib_list[2]
    fib_list = fib_list[1:] + [sum(fib_list[1:])]

# print result
print(total)

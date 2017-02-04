"""Find the sum of all numbers that are equal to the sum of 5th powers of their digits. Exclude 1-digit numbers."""


def sum_digits_power5(n):
    """return sum of 5th power of digits of int n"""
    c = 0
    for a in str(n):
        c += int(a) ** 5
    return c

# set upper bound for brute-force search, increase it if answer is wrong
upper_bound = 1000000
numbers = []

for x in range(10, upper_bound):
    if x == sum_digits_power5(x):
        numbers.append(x)

print(numbers, sum(numbers))

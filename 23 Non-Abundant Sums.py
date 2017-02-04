"""Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. The upper
bound for the largest number that cannot be written as the sum of two abundant numbers is 28123"""


def proper_factors(n):
    """return list containing all proper factors of n"""
    factor_set = set()
    for a in range(1, int(n**0.5)+1):
        if n % a == 0:
            factor_set.add(a)
            factor_set.add(n // a)
    factor_list = list(factor_set)
    factor_list.sort()
    proper_factor_list = factor_list[:-1]
    return proper_factor_list


# find all abundant numbers <= 28123
abundant_numbers = []
for x in range(1, 28124):
    if sum(proper_factors(x)) > x:
        abundant_numbers.append(x)

# find all numbers <= 28123 that can be expressed as sum of 2 abundant numbers
sum_of_2_abundant_numbers = set()
for x in range(len(abundant_numbers)):
    for y in range(x, len(abundant_numbers)):
        if abundant_numbers[x] + abundant_numbers[y] <= 28123:
            sum_of_2_abundant_numbers.add(abundant_numbers[x] + abundant_numbers[y])

# find all numbers <= 28123 that can't be expressed as sum of 2 numbers
not_sum_of_2_abundant_numbers = list(set(range(1, 28124)) - sum_of_2_abundant_numbers)

print(sum(not_sum_of_2_abundant_numbers))

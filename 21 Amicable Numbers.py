"""Calculate sum of all amicable numbers less than 10000"""


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


amicable_numbers = set()

# make list of the sum of proper factors for each integer between 1 and 9999, inclusive
proper_factor_sums = [sum(proper_factors(x)) for x in range(1, 10000)]

# For each element in proper_factor_sums, determine whether its proper factor sum is equal to its 1-based position in
# list and if the element is not equal to its 1-based position in list. If both are true, the element and its position
# are an amicable pair. The reason for excluding elements that are equal to their 1-based positions in the list is to
# exclude perfect numbers.
for a in range(9999):
    if proper_factor_sums[a] != a + 1 < 9999 and sum(proper_factors(proper_factor_sums[a])) == a + 1:
        amicable_numbers.add(proper_factor_sums[a])
        amicable_numbers.add(a + 1)

print(sum(amicable_numbers))

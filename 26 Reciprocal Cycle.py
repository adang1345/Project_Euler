"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""


def contains_more_than_empty_strings(l):
    """determines whether each element except the last of list l contains only empty strings"""
    for a in l[:-1]:
        if a != "":
            return True
    return False


def pattern_length(n, num_of_digits, max_prefix_length):
    """Finds length of recurring cycle of 1/n, assuming that recursion happens at least twice by the time num_of_digits
    after decimal point is reached and that the cycle begins at most max_prefix_length after decimal point. If there
    is no recurring cycle, returns 0."""
    if 10 ** num_of_digits % n == 0:
        return 0
    digits = str(10 ** num_of_digits // n)
    for start_cycle in range(max_prefix_length + 1):
        end_cycle = start_cycle + 1
        while True:
            if end_cycle == len(digits):
                break
            elif contains_more_than_empty_strings(digits[start_cycle:].split(digits[start_cycle: end_cycle])):
                end_cycle += 1
            else:
                return end_cycle - start_cycle

max_length = 0
n_value = 1
for x in range(1, 1000):
    candidate = pattern_length(x, 5000, 1000)
    if candidate > max_length:
        max_length = candidate
        n_value = x

print(n_value)

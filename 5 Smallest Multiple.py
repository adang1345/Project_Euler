"""Computes the smallest number that is divisible by 1 through 20"""

def isdivisible(num):
    """Determines whether num is divisible by 1 through 20. If and only if num is divisible by 11, 13, 14, 16, 17, 18,
    19, and 20, then num must be divisible by all numbers from 1 through 20. Assume num is a positive integer."""
    for divisor in [11, 13, 14, 16, 17, 18, 19, 20]:
        if num % divisor != 0:
            return False
    return True

# Answer is known to be larger than 2520, which is divisible by 20. Start at 2520 and test whether it is divisible by
# all numbers from 1 to 20. If not, start testing the integer 20 greater.
a = 2520
while not isdivisible(a):
    a += 20

# perform final test and raise error if answer given is wrong
for x in range(1, 21):
    if a % x != 0:
        raise Exception("Logical error in code.")

print(a)

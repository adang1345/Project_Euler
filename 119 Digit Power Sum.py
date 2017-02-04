"""The number 512 is interesting because it is equal to the sum of its digits raised to some power:
5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have
a sum.

You are given that a(2) = 512 and a(10) = 614656.

Find a(30)."""


def sum_digits(n):
    """Return the sum of the digits of int n."""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


exponent_limit = 100
base_limit = 100
powers = set()

for base in range(1, base_limit+1):
    for exponent in range(1, exponent_limit+1):
        powers.add((base, base ** exponent))

digit_power_sums = [y for (x,y) in powers if sum_digits(y) == x and y > 9]
digit_power_sums.sort()
print(digit_power_sums[29])

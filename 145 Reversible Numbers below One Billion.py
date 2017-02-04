"""Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are
reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?"""


def is_reversible(n):
    str_n = str(n)
    if n % 10 == 0:
        return False
    if (int(str_n[0]) + int(str_n[-1])) % 2 != 1:
        return False
    for digit in str(int(str_n) + int(str_n[::-1])):
        if int(digit) % 2 == 0:
            return False
    return True


c = 0
for x in range(1, 10 ** 9):
    if is_reversible(x):
        c += 1

print(c)

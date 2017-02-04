"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""


total = 0
for x in range(1, 1000000):
    x_str = str(x)
    if x_str == x_str[::-1] and "{0:b}".format(x) == "{0:b}".format(x)[::-1]:
        total += x

print(total)

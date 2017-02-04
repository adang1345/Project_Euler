"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000"""

n = 0
c = ""
while len(c) < 1000001:
    c += str(n)
    n += 1

print(int(c[1]) * int(c[10]) * int(c[100]) * int(c[1000]) * int(c[10000]) * int(c[100000]) * int(c[1000000]))

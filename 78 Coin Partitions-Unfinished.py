"""Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins
can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million."""

# I ported the following code from another person's C# implementation. I found it too difficult to code an answer on my
# own.

p = [1]
n = 1

while True:
    i = 0
    penta = 1
    p.append(0)

    while penta <= n:
        if i % 4 > 1:
            sign = -1
        else:
            sign = 1
        p[n] += sign * p[n - penta]
        p[n] %= 1000000
        i += 1

        if i % 2 == 0:
            j = i // 2 + 1
        else:
            j = -(i // 2 + 1)
        penta = j * (3 * j - 1) // 2

    if p[n] == 0:
        break
    n += 1

print(n)

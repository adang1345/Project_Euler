"""A number chain is created by continuously adding the square of the digits in a number to form a new number until it
has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?"""


def square_digits(n):
    """Return the sum of the squares of the digits of int n."""
    s = 0
    for x in str(n):
        s += int(x) ** 2
    return s


def chain_end(n):
    """Return the end of the square digit chain of n, either 1 or 89."""
    while n != 1 and n != 89:
        n = square_digits(n)
    return n


c = 0
for x in range(1, 10000000):
    if chain_end(x) == 89:
        c += 1

print(c)

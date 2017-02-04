"""Find the sequence index of the first Fibonacci number with 1000 digits"""

# start with list containing first 2 Fibonacci numbers

from math import log10


def num_digits(n):
    """returns number of digits in int n"""
    return int(log10(n)) + 1

# list out Fibonacci numbers until reaching one with 1000 digits
fib_list = [1, 1]
while num_digits(fib_list[-1]) < 1000:
    fib_list.append(fib_list[-2] + fib_list[-1])

print(len(fib_list))

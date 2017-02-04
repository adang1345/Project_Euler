"""By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is
part of an eight prime value family."""

from itertools import combinations


def is_prime(num):
    """Determine whether num is prime.
    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def eight_primes(l):
    """Return True if at least 8 ints in list l are prime."""
    num_primes = 0
    for p in l:
        if is_prime(p):
            num_primes += 1
    return num_primes >= 8


def replace_digits(n, d):
    """For int n and tuple d, return list of value family for n by replacing digit numbers represented by d."""
    list_n = [int(x) for x in str(n)]
    value_family = []
    for replacement in range(10):
        for digit in d:
            list_n[digit] = replacement
        if list_n[0] != 0:
            value_family.append(int("".join([str(x) for x in list_n])))
    return value_family


def which_digits(n):
    """Return list of tuples containing which digit numbers can be changed simultaneously in int n."""
    num_digits = len(str(n))
    digit_combos = []
    for x in range(1, num_digits):
        digit_combos += list(combinations(range(num_digits), x))
    return digit_combos


def has_good_value_family(n):
    """Return True if n has a value family with 8 primes."""
    for digit_combo in which_digits(n):
        if eight_primes(replace_digits(n, digit_combo)):
            return True
    return False

x = 2
while True:
    if is_prime(x) and has_good_value_family(x):
        print(x)
        break
    x += 1

for digit_combo in which_digits(120383):
    if eight_primes(replace_digits(120383, digit_combo)):
         print(replace_digits(120383, digit_combo))

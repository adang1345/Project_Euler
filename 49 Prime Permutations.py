"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one
other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""


def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def are_permutations(a, b, c):
    """Test whether ints a, b, and c have digits that are permutations of each other. Assume 1001 <= a,b,c <= 9999."""
    return set(str(a)) == set(str(b)) == set(str(c))


for a in range(1001, 9996, 2):  # arithmetic sequence must begin with odd number
    if a == 1487:
        continue
    if isprime(a):
        for b in range(a + 2, 9998, 2):
            c = 2 * b - a
            if isprime(b) and isprime(c) and are_permutations(a, b, c) and c < 10000:
                print(str(a) + str(b) + str(2*b-a))

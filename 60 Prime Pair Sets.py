"""The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime."""


def is_prime(num):
    """Determine whether num is prime.
    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def prime_after(n):
    """return smallest prime greater than n"""
    n += 1
    while not is_prime(n):
        n += 1
    return n


def concatenate(a, b):
    """Return a concatenation of ints a and b."""
    return int(str(a) + str(b))


def concatenate_prime(a, b):
    """Return True if a and b concatenate in either order to form primes, False otherwise."""
    return is_prime(concatenate(a, b)) and is_prime(concatenate(b, a))


# generate list of primes up to 100000
primes = [2]
while primes[-1] < 10000:
    primes.append(prime_after(primes[-1]))

# search for 5 primes that concatenate
for p1 in range(len(primes)):
    for p2 in range(p1 + 1, len(primes)):
        if concatenate_prime(primes[p1], primes[p2]):
            for p3 in range(p2 + 1, len(primes)):
                if concatenate_prime(primes[p1], primes[p3]) and concatenate_prime(primes[p2], primes[p3]):
                    for p4 in range(p3 + 1, len(primes)):
                        if concatenate_prime(primes[p1], primes[p4]) and concatenate_prime(primes[p2], primes[p4]) and concatenate_prime(primes[p3], primes[p4]):
                            for p5 in range(p4 + 1, len(primes)):
                                if concatenate_prime(primes[p1], primes[p5]) and concatenate_prime(primes[p2], primes[p5]) and concatenate_prime(primes[p3], primes[p5]) and concatenate_prime(primes[p4], primes[p5]):
                                    answer = [primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]]
                                    print(answer, sum(answer))
                                    break

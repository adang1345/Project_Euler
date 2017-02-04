"""The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact,
there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth
power?"""


def prime_sieve(n):
    """Return a list of all prime numbers less than or equal to n."""
    primes = [2]
    for x in range(3, n + 1):
        if is_prime(x, primes):
            primes.append(x)
    return primes


def is_prime(p, primes):
    """Return whether p is prime. primes must be a list of all primes less than p."""
    for x in primes:
        if p % x == 0:
            return False
        if x > p ** 0.5:
            return True
    return True


expressables = set()
primes1 = prime_sieve(7071)
primes2 = prime_sieve(368)
primes3 = prime_sieve(84)

for x in primes1:
    for y in primes2:
        for z in primes3:
            expressable = x**2 + y**3 + z**4
            if expressable < 50000000:
                expressables.add(expressable)

print(len(expressables))

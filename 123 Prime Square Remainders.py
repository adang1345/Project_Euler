"""Let p(n) be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (p(n)−1)^n + (p(n)+1)^n is divided
by p(n)^2.

For example, when n = 3, p(3) = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037. Find the least value of n for which the
remainder first exceeds 10^10."""


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


def r(n, p):
    if n % 2 == 1:
        return 2 * p * n
    return 2


primes = ["filler"] + prime_sieve(1000000)
for x in range(1, len(primes)):
    if r(x, primes[x]) > 10 ** 10:
        print(x)
        break

"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""


def isprime(num):
    """Determine whether num is prime.
    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def next_prime(n):
    """Return smallest prime greater than n."""
    n += 1
    while not isprime(n):
        n += 1
    return n

# make list of consecutive primes with sum less than 2000000
primes = [2]
while sum(primes) < 2000000:
    primes.append(next_prime(primes[-1]))
if sum(primes) > 2000000:
    del primes[-1]

max_addends = 2
max_prime_sum = 2

for x in range(len(primes)):
    for y in range(x + 1, len(primes)):
        prime_sum = sum(primes[x: y])
        if prime_sum > 1000000:
            break
        elif y - x + 1 > max_addends and isprime(prime_sum):
            max_addends = y - x + 1
            max_prime_sum = prime_sum

print(max_prime_sum)

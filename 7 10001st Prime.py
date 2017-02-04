"""Computes the 10001st prime number"""

def isprime(num):
    """Determine whether num is prime.

    If any integer from 2 to the square root of num divides evenly into num, then num is composite.
    Otherwise, num is prime. Assume that num is an int greater than or equal to 2."""

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

# Start counter at 0 and end when it reaches 10001. Increment the counter by 1 if a prime number is found.
count = 0
prime_candidate = 2
while count < 10001:
    if isprime(prime_candidate):
        count += 1
    prime_candidate += 1

# Due to how the loop was constructed, an extra 1 is added to the prime candidate at the end. Subtract 1 to reveal
# the answer.
print(prime_candidate - 1)

"""Computes the largest palindrome integer that is the product of two 3-digit numbers"""

def is_palindrome(candidate):
    """determine whether the int candidate is a palindrome"""
    candidate = str(candidate)
    return candidate == candidate[::-1]

# Set answer to a value that is known to be less than the solution. For each pair of 3-digit numbers, test whether
# their product is a palindrome and is greater than answer. If so, set answer equal to that product.
answer = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if is_palindrome(product) and product > answer:
            answer = product

print(answer)

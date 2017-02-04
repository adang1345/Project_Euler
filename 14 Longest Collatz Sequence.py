"""Find the starting number under 1 million that produces the longest Collatz chain"""

def collatz_chain_length(n):
    """Return the Collatz chain length for n. Assume n is int greater than 1."""
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
            length += 1
        else:
            n = (3*n + 1) // 2
            length += 2
    return length


max_length = 1
starting_number = 2
for x in range(2, 1000000):
    candidate = collatz_chain_length(x)
    if candidate > max_length:
        max_length = candidate
        starting_number = x

print(starting_number)

"""Prints the sum of all multiples of 3 or 5 below 1000"""

print(sum([x for x in range(1, 1000) if x%3==0 or x%5==0]))

"""Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors. For
example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15."""


def factors(n):
    """return set containing all factors of n"""
    factor_set = set()
    for a in range(1, int(n**0.5)+1):
        if n % a == 0:
            factor_set.add(a)
            factor_set.add(n // a)
    return factor_set


def num_factors(n):
    """Return the number of factors of n."""
    return len(factors(n))

factor_counts = []
for n in range(2, 10 ** 7 + 2):
    factor_counts.append(num_factors(n))

c = 0
for x in range(len(factor_counts)-1):
    if factor_counts[x] == factor_counts[x+1]:
        c += 1

print(c)

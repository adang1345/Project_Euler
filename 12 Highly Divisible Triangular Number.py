"""Find the smallest triangular number with over 500 divisors."""

def triangular(n):
    """return the nth triangular number"""
    return n * (n+1) // 2


def factors(n):
    """return set containing all factors of n"""
    factor_set = set()
    for a in range(1, int(n**0.5)+1):
        if n % a == 0:
            factor_set.add(a)
            factor_set.add(n // a)
    return factor_set

n = 1
while len(factors(triangular(n))) <= 500:
    n += 1

print(triangular(n))

"""Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n?1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n?1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal."""


def is_pentagonal(n):
    """determine whether n is a pentagonal number"""
    x = (((24*n + 1) ** 0.5) + 1) // 6
    return x * (3*x-1) // 2 == n


def is_triangular(n):
    """determine whether n is a triangular number"""
    x = ((8*n+1) ** 0.5 - 1) // 2
    return x * (x + 1) // 2 == n


def is_pentagonal_and_triangular(n):
    """determine whether n is triangular and pentagonal"""
    return is_pentagonal(n) and is_triangular(n)


def hexagonal(n):
    """return nth hexagonal number"""
    return n * (2*n-1)


n = 144
while not is_pentagonal_and_triangular(hexagonal(n)):
    n += 1
print(hexagonal(n))

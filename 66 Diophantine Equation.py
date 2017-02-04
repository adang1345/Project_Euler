"""Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square. By finding minimal solutions in x
for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained."""


def continued_fraction(s, p):
    """Return the first p elements of the continued fraction expansion of the sqrt of n. The expression is a list in the
    following form: [n1, n2, n3,...,np]
    This algorithm was developed from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm.

    Preconditions: s is not a perfect square. p is a positive int"""
    m = 0
    d = 1
    a = [int(s ** 0.5)]
    for _ in range(p-1):
        m = d * a[-1] - m
        d = (s - m ** 2) // d
        a.append((a[0] + m) // d)
    return a


def minimal_solution(d):
    """Return the smallest integer x for which x^2 - d*y^2 = 1 has a solution in the positive integers.

    This problem is solved by performing a continued fraction expansion of sqrt(d). The minimal solution is the
    numerator of the first convergent to sqrt(d) for which setting x = convergent's numerator and setting
    y = convergent's denominator satisifies the equation. Here, I assume that such a convergent will be found in the
    first 100 convergents from the continued fraction expansion."""
    cf = continued_fraction(d, 100)
    n = 0
    h = [0, 1, cf[0]]
    k = [1, 0, 1]
    while h[-1] ** 2 - d * k[-1] ** 2 != 1:
        n += 1
        h.append(cf[n] * h[-1] + h[-2])
        k.append(cf[n] * k[-1] + k[-2])
    return h[-1]


# Generate list of non-square numbers in 1..1000
non_squares = [x for x in range(1, 1001) if int(x**0.5)**2 != x]
max_x = 0
max_d = 0
for d in non_squares:
    c = minimal_solution(d)
    if c > max_x:
        max_x = c
        max_d = d

print("The answer is " + str(max_d))

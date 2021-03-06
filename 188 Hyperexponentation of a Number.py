"""The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and 3↑↑4 is roughly 10^(3.6383346400240996*10^12).

Find the last 8 digits of 1777↑↑1855."""


def tetration(a, b, m):
    t0 = 1
    for i in range(b):
        t1 = pow(a, t0, m)
        if t0 == t1:
            break
        t0 = t1
    return t1

print("Project Euler 188 Solution = %08d" % tetration(1777, 1855, 10**8))

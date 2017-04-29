import functools


@functools.lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return 1
    elif n == 3:
        return 3
    elif n % 2 == 0:
        return f(n//2)
    elif n % 4 == 1:
        return 2 * f((n-1)//2+1) - f((n-1)//4)
    else:
        return 3 * f((n-3)//2+1) - 2 * f((n-3)//4)

for i in range(1, 1000000):
    print(f(i))

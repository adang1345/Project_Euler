"""https://projecteuler.net/problem=303"""

LIMIT = 10000

total = 0
ns = list(range(1, LIMIT + 1))
zero_one_two = [1, 2]

# I found through experimentation that if n contains only the digit 9, then f(n)/n can be computed quickly.
new_ns = []
for n in ns:
    digits = set(str(n))
    if digits == {"9"}:
        # If n contains just the digit 9, then f(n)/n can be computed quickly. Discovered through experimentation.
        d = len(str(n))
        total += int("1"*d + "3"*d + "5"*d + "7"*(d-1) + "8")
    elif digits <= {"0", "1", "2"}:
        # If n already contains only digits <= 2, then f(n)/n is 1.
        total += 1
    else:
        new_ns.append(n)
ns = new_ns

while len(ns) > 0:
    new_ns = []
    removed = set()
    new_zero_one_two = []

    for f in zero_one_two:
        for n in ns:
            if f % n == 0 and n not in removed:
                total += f // n
                removed.add(n)

    for n in ns:
        if n not in removed:
            new_ns.append(n)
    ns = new_ns

    for i in zero_one_two:
        new_zero_one_two.append(i * 10)
        new_zero_one_two.append(i * 10 + 1)
        new_zero_one_two.append(i * 10 + 2)
    zero_one_two = new_zero_one_two
    print(len(zero_one_two))

print(total)

"""https://projecteuler.net/problem=150

For each number in the triangle, I find the minimum-sum triangle with top corner at that number. Then I take the global
minimum of all of these."""


def min_with_head(row, col, s):
    """Return the smallest subtriangle sum in s that has head at (row, col)."""
    m = s[row][col]
    cumsum = m
    row_offset = 0
    while True:
        row_offset += 1
        try:
            cumsum += sum(s[row + row_offset][col: col+row_offset+1])
            m = min(m, cumsum)
        except IndexError:
            return m


beginning_of_row = {round(x**2/2 + x/2 + 1) for x in range(1001)}
s = []
t = 0
for k in range(1, 500_501):
    t = (615949 * t + 797807) % 1048576
    if k in beginning_of_row:
        s.append([t - 524288])
    else:
        s[-1].append(t - 524288)

m = s[0][0]
for row in range(1000):
    for col in range(row + 1):
        m = min(m, min_with_head(row, col, s))
print(m)

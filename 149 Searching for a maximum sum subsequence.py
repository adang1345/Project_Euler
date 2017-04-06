"""https://projecteuler.net/problem=149"""


def max_subsequence_sum(a):
    """Given list a, return the maximum subsequence sum."""
    max_ending_here = max_so_far = a[0]
    for x in a[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


size = 2000

# generate pseudorandom numbers
s = []
for k in range(1, 56):
    s.append((100003 - 200003*k + 300007*k**3) % 1000000 - 500000)
for k in range(56, 4000001):
    s.append((s[k-25] + s[k-56] + 1000000) % 1000000 - 500000)

max_sum = 0

# rows
for r in range(size):
    row = s[r*size : (r+1)*size]
    max_sum = max(max_sum, max_subsequence_sum(row))

# columns
for c in range(size):
    column = [s[c+size*n] for n in range(size)]
    max_sum = max(max_sum, max_subsequence_sum(column))
s2 = [s[r*size : (r+1)*size] for r in range(size)]  # convert to 2D list

# diagonals
first_index = [0, size-1]
while first_index[1] > 0:
    # print(first_index, end=" ")
    diagonal = [s2[first_index[0]][first_index[1]]]
    next_index = [first_index[0]+1, first_index[1]+1]
    while next_index[1] < size:
        diagonal.append(s2[next_index[0]][next_index[1]])
        next_index = [next_index[0]+1, next_index[1]+1]
    # print(len(diagonal))
    max_sum = max(max_sum, max_subsequence_sum(diagonal))
    first_index[1] -= 1
while first_index[0] < size:
    # print(first_index, end=" ")
    diagonal = [s2[first_index[0]][first_index[1]]]
    next_index = [first_index[0]+1, first_index[1]+1]
    while next_index[0] < size:
        diagonal.append(s2[next_index[0]][next_index[1]])
        next_index = [next_index[0]+1, next_index[1]+1]
    # print(len(diagonal))
    max_sum = max(max_sum, max_subsequence_sum(diagonal))
    first_index[0] += 1

# antidiagonals
first_index = [0, 0]
while first_index[0] < size-1:
    # print(first_index, end=" ")
    diagonal = [s2[first_index[0]][first_index[1]]]
    next_index = [first_index[0]-1, first_index[1]+1]
    while next_index[0] >= 0:
        diagonal.append(s2[next_index[0]][next_index[1]])
        next_index = [next_index[0]-1, next_index[1]+1]
    # print(len(diagonal))
    max_sum = max(max_sum, max_subsequence_sum(diagonal))
    first_index[0] += 1
while first_index[1] < size:
    # print(first_index, end=" ")
    diagonal = [s2[first_index[0]][first_index[1]]]
    next_index = [first_index[0]-1, first_index[1]+1]
    while next_index[1] < size:
        diagonal.append(s2[next_index[0]][next_index[1]])
        next_index = [next_index[0]-1, next_index[1]+1]
    # print(len(diagonal))
    max_sum = max(max_sum, max_subsequence_sum(diagonal))
    first_index[1] += 1

print(max_sum)

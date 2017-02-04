"""https://projecteuler.net/problem=138
For the case where the h = b+1, we must solve the Diophantine equation 5b^2 - 4L^2 + 8b + 4 = 0. Its minimal solution is
b = 272, L = 305, as stated in the problem.
From https://www.alpertron.com.ar/QUAD.HTM, the next solutions are given by
b[n+1] = -9*b[n] - 8*L[n] - 8
L[n+1] = -10*b[n] -9*L[n] - 8

For the case where h = b-1, we must solve the Diophantine equation 5b^2 - 4L^2 - 8b + 4 = 0. Its minimal solution is
b = 16, L = 17, as stated in the problem. The next solutions are given by
b[n+1] = -9*b[n] - 8*L[n] + 8
L[n+1] = -10*b[n] - 9*L[n] + 8
"""


# generate list of (base, leg) tuples for 12 smallest "h=b+1" triangles and 12 smallest "h=b+1" triangles
b = [272]
l = [305]
b2 = [16]
l2 = [17]
for _ in range(22):
    bn = b[-1]
    ln = l[-1]
    b.append(-9*bn - 8*ln - 8)
    l.append(-10*bn - 9*ln - 8)
    bn2 = b2[-1]
    ln2 = l2[-1]
    b2.append(-9 * bn2 - 8 * ln2 + 8)
    l2.append(-10 * bn2 - 9 * ln2 + 8)
b.extend(b2)
l.extend(l2)

special_triangles = [x for x in zip(b, l) if x[0] > 0 and x[1] > 0]  # consider only positive side lengths

# Sort by base. Since area is approximately base^2/2, this should also sort triangles by area.
special_triangles.sort()

# Take the smallest 12 triangles and print the sum of their legs.
print(sum(x[1] for x in special_triangles[:12]))

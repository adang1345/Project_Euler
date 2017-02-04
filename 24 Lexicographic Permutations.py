"""Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9. That is, take the list
of all permutations of these digits in order from smallest to largest. What is the millionth number in this list?"""

from itertools import permutations

# find all permutations of "0123456789" and sort them
perms = ["".join(a) for a in permutations("0123456789")]
perms.sort()

print(perms[999999])

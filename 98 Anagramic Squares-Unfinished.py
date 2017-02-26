"""https://projecteuler.net/problem=98"""
from itertools import combinations


def are_anagrams(s1, s2):
    """Return whether strings s1 and s2 are anagrams."""
    if len(s1) != len(s2):
        return False
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()
    return l1 == l2


words = eval("{" + open("98 Words.txt").read() + "}")
word_pairs = combinations(words, 2)
anagramic_pairs = [x for x in word_pairs if are_anagrams(x[0], x[1])]
print(anagramic_pairs[:10])

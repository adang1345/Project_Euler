"""https://projecteuler.net/problem=98"""
from itertools import combinations, permutations


def are_anagrams(s1, s2):
    """Return whether strings s1 and s2 are anagrams."""
    if len(s1) != len(s2):
        return False
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()
    return l1 == l2


def letter_to_number(s1, s2):
    """Given two anagramic strings s1 and s2, return a list of all dictionaries that can map each letter in s1 to a
    number such that the first letter of s1 and the first letter of s2 both do not map to 0, and no two letters map to
    the same number."""
    all_dicts = []
    letters = tuple(set(s1))
    number_permutations = permutations(range(10), len(letters))
    for n in number_permutations:
        if len(set(n)) != len(n):  # ensure no 2 letters map to same number
            continue
        d = {}
        for x in range(len(letters)):
            d[letters[x]] = n[x]
        if d[s1[0]] != 0 and d[s2[0]] != 0:  # ensure 1st letter doesn't map to 0
            all_dicts.append(d)
    return all_dicts


def map_to_number(s, d):
    """Given a mapping d from letters to numbers, provide the value of string s.
    Precondition: Every letter in s is a key of dictionary d."""
    v = 0
    for letter in s:
        v = v * 10 + d[letter]
    return v


words = eval("{" + open("98 Words.txt").read() + "}")
word_pairs = combinations(words, 2)
anagramic_pairs = [x for x in word_pairs if are_anagrams(x[0], x[1])]
squares = {x**2 for x in range(1, 31622)}

largest_square = 0
for pair in anagramic_pairs:
    for map in letter_to_number(pair[0], pair[1]):
        cand1 = map_to_number(pair[0], map)
        cand2 = map_to_number(pair[1], map)
        if cand1 in squares and cand2 in squares:
            if cand1 > largest_square:
                largest_square = cand1
            if cand2 > largest_square:
                largest_square = cand2
print(largest_square)

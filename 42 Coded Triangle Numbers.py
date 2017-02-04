"""The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using "42_words.txt", a file containing nearly two-thousand common English words, how many are triangle words?"""


def score(name):
    """Return score of a name, which is sum of alphabetical position for each letter in name. Assume name contains only
    capital letters."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 0
    for a in name:
        c += alphabet.index(a) + 1
    return c


# generate 1000 triangle numbers
triangle_numbers = []
for x in range(1, 1001):
    triangle_numbers.append(x * (x + 1) // 2)

# read 42_words.txt file and make list containing all words
words_file = open("42_words.txt")
words = words_file.read().replace('"', "").split(",")
words_file.close()

# count number of words with triangular values
c = 0
for word in words:
    if score(word) in triangle_numbers:
        c += 1

print(c)

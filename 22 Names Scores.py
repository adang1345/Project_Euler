"""Using 22_names.txt, a text file containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?"""


def score(name):
    """Return score of a name, which is sum of alphabetical position for each letter in name. Assume name contains only
    capital letters."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 0
    for a in name:
        c += alphabet.index(a) + 1
    return c

# open 22_names.txt and generate list containing all names
names_file = open("22_names.txt")
names_list = names_file.read().replace('"', "").split(",")

# sort list of names into alphabetical order
names_list.sort()

# find sum of products of name score and position in list
total = 0
for index, name in enumerate(names_list):
    total += score(name) * (index + 1)

print(total)

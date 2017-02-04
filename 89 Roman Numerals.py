"""For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even
though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a
particular number. For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units."""


def optimize(n):
    """Return the optimized form of Roman numeral n."""
    n = n.replace("VIIII", "IX")
    n = n.replace("IIII", "IV")
    n = n.replace("LXXXX", "XC")
    n = n.replace("XXXX", "XL")
    n = n.replace("DCCCC", "CM")
    n = n.replace("CCCC", "CD")
    return n


f = open("89 Roman.txt")
t = f.read()
f.close()
old_length = len(t)
new_length = len(optimize(t))

print(old_length - new_length)

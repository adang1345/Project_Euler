"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital. The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital. Find the sum of all products whose
multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."""

def factor_pairs(n):
    """return list of tuples; each tuple is a factor pair of n"""
    factor_pair_list = []
    for a in range(1, int(n**0.5)+1):
        if n % a == 0:
            factor_pair_list.append((a, n//a))
    return factor_pair_list


def is_pandigital(n):
    """for int n, determines whether n can be written as pandigital product"""
    for factor_pair in factor_pairs(n):
        whole_eq = str(factor_pair[0]) + str(factor_pair[1]) + str(n)
        if (whole_eq.count("1") == whole_eq.count("2") == whole_eq.count("3") == whole_eq.count("4") ==
                whole_eq.count("5") == whole_eq.count("6") == whole_eq.count("7") == whole_eq.count("8") ==
                whole_eq.count("9") == 1 and whole_eq.count("0") == 0):
            return True
    return False

c = 0
for x in range(1, 100000):  # test pandigitality of equations for products up to 999999 and find sum of these products
    if is_pandigital(x):
        c += x

print(c)

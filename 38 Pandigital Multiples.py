"""Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
of 192 and (1,2,3). The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?"""

# The integer (which I will call p) that is multiplied by (1, ... , n) cannot have more digits than 4 if p leads to a
# pandigital 9-digit number with the properties specified. Given that n is at least 2, a 5-digit p would lead to a
# concatenation of p*1 and p*2, which would have either 10 or 11 digits. Therefore, 1 <= p <= 9999. I will use each p
# in this interval to determine which results in the largest pandigital 9-digit number.


def pandigital(p):
    """Determines whether int p can generate a 9-digit pandigital number using the algorithm above. If so, returns this
    pandigital number. If not, returns 0."""
    n = 1
    a = ""
    while len(a) < 9:
        a += str(p * n)
        n += 1
    if (a.count("1") == a.count("2") == a.count("3") == a.count("4") == a.count("5") == a.count("6") == a.count("7")
         == a.count("8") == a.count("9") == 1 and a.count("0") == 0):
        return int(a)
    else:
        return 0


pandigital_number = 123456789
for p in range(1, 10000):
    pandigital_number = max(pandigital_number, pandigital(p))

print(pandigital_number)

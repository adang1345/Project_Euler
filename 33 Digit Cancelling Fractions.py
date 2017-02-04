"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator. If the product of these four fractions is given in its lowest common terms, find the
value of the denominator."""

from fractions import gcd


def share_nonzero_digit(num, den):
    """Determine whether 2-digit numbers num and den share a nonzero digit"""
    num_str = str(num)
    den_str = str(den)
    if "0" in num_str and "0" in den_str:
        return False
    return num_str[0] in den_str or num_str[1] in den_str


def can_cancel(num, den):
    """For two 2-digit numbers num and den sharing a nonzero digit, determines whether these digits can cancel and
    maintain the value of num/den"""
    num_str = str(num)
    den_str = str(den)
    if num_str[0] == den_str[0] and den_str[1] != "0":
        return num / den == int(num_str[1]) / int(den_str[1])
    elif num_str[0] == den_str[1] and den_str[0] != "0":
        return num / den == int(num_str[1]) / int(den_str[0])
    elif num_str[1] == den_str[0] and den_str[1] != "0":
        return num / den == int(num_str[0]) / int(den_str[1])
    elif num_str[1] == den_str[1] and den_str[0] != "0":
        return num / den == int(num_str[0]) / int(den_str[0])
    else:
        return False


numerator_product = denominator_product = 1
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if share_nonzero_digit(numerator, denominator) and can_cancel(numerator, denominator):
            numerator_product *= numerator
            denominator_product *= denominator

denominator_product //= gcd(numerator_product, denominator_product)
print(denominator_product)

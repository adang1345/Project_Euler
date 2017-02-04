"""The palindromic number 595 is interesting because it can be written as the sum of consecutive squares:
6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of
these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares
of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive
squares."""


def is_palindrome(n):
    """Return whether int n is a palindromic number."""
    n = str(n)
    return n == n[::-1]


limit = 10 ** 8
sqrt_limit = 7072

sum_squares = set()
for start_square in range(1, sqrt_limit):
    current_sum = start_square ** 2
    for end_square in range(start_square+1, sqrt_limit):
        current_sum = current_sum + end_square ** 2
        if current_sum < limit:
            sum_squares.add(current_sum)

palindromic_sum_squares = [x for x in sum_squares if is_palindrome(x)]
print(sum(palindromic_sum_squares))

"""Computes difference between squared sum of 1-100 and sum of squares of 1-100"""

def sum_of_squares(n):
    """return sum of squares of 1st n natural numbers"""
    return n * (n + 1) * (2*n + 1) // 6


def square_of_sum(n):
    """return square of sum of 1st n natural numbers"""
    return n**2 * (n + 1)**2 // 4

print(square_of_sum(100) - sum_of_squares(100))

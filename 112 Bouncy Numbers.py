"""Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for
example, 66420. We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for
example, 155349. Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is
538. Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy
numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%."""

import functools


@functools.lru_cache(maxsize=None)
def is_bouncy(n):
    """Return True if n is a bouncy number."""
    increasing = True
    decreasing = True
    n = str(n)
    for digit_num in range(1, len(n)):
        if int(n[digit_num] > n[digit_num-1]):
            decreasing = False
        elif int(n[digit_num] < n[digit_num-1]):
            increasing = False
        if not increasing and not decreasing:
            return True
    return False


def bouncy_proportion(n):
    """Return the number of bouncy numbers less than or equal to n"""
    c = 0
    for x in range(n+1):
        if is_bouncy(x):
            c += 1
    return c / n

lower = 1000000
upper = 5000000
guess = int(round((lower+upper) / 2, -2))
bouncyproportion = bouncy_proportion(guess)
while bouncyproportion != 0.99:
    if bouncyproportion < 0.99:
        lower = guess
    else:
        upper = guess
    guess = int(round((lower + upper) / 2, -2))
    bouncyproportion = bouncy_proportion(guess)
    print(guess)

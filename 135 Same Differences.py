"""https://projecteuler.net/problem=135

Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the
positive integer, n, for which the equation, x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?


Consider the equation x^2 - (x-a)^2 - (x-2a)^2 = n. This factors into (x-a)(5a-x)=n. Since x-a must be positive,
5a-x must also be positive. So we should find positive factor pairs of n to get closer to a solution. Using linear
algebra, I showed that if n=c1*c2, where c1 and c2 are positive integers, then
x = (5*c1+c2)/4 and a = (c1+c2)/4.
In addition, x-2a > 0, so 3*c1 > c2.
Now I have shown that the number of solutions to x^2 − y^2 − z^2 = n is the number of factor pairs (c1,c2) of n such
that c1+c2 is divisible by 4 and 3*c1 > c2.
"""


def num_solutions(n):
    """Count the number of positive integer solutions to x^2 − y^2 − z^2 = n."""
    count = 0
    for x in range(1, int(n**0.5)+1):
        cand = (x, n // x)
        if n % x == 0 and sum(cand) % 4 == 0:
            if 3*cand[0] > cand[1]:
                count += 1
            if 3*cand[1] > cand[0] and cand[1] != cand[0]:
                count += 1
    return count


c = 0
for n in range(1, 1000000):
    if num_solutions(n) == 10:
        c += 1
print("The answer is " + str(c))

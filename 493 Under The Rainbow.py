"""https://projecteuler.net/problem=493

The probability that a red ball is not picked is C(60,20) / C(70,20).
The probability that a red ball is picked is 1 - C(60,20) / C(70,20). Let P be this value.

Let R be a Bernoulli random variable indicating whether a red ball is picked. E[R] = P.
There are 7 colors, so the expected number of colors chosen is E[7R] = 7E[R] = 7P."""

import euler

ans = 7 * (1 - euler.choose(60, 20) / euler.choose(70, 20))
print(round(ans, 9))

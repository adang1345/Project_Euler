"""Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that
2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over
three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above."""

import math

logs = []
for line in open("99 Largest Exponential.txt"):
    nums = [int(x) for x in line.rstrip("\n").split(",")]
    logs.append(nums[1] * math.log(nums[0]))

print(logs.index(max(logs)) + 1)

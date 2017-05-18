"""https://projecteuler.net/problem=121"""

import fractions
import itertools


num_turns = 15

# construct probabilies of getting a blue disk for each turn
blue_disk_prob = [fractions.Fraction(1, n) for n in range(2, num_turns+2)]

# find the minimum number of blue disks needed to win
if num_turns % 2 == 0:
    min_win_count = num_turns // 2 + 1
else:
    min_win_count = (num_turns + 1) // 2

# calculate the probability of winning
s = 0
for win_count in range(min_win_count, num_turns+1):
    for combo in itertools.combinations(range(num_turns), win_count):
        p = 1
        for x in range(num_turns):
            if x in combo:
                p *= blue_disk_prob[x]
            else:
                p *= 1 - blue_disk_prob[x]
        s += p

print(int(1 / s))

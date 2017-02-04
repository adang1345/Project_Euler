"""Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are
equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the
form 0.abcdefg"""

# obtain the number of ways to get each sum with 9 pyramidal dice
pyramidal = {}
for x in range(9, 37):
    pyramidal[x] = 0
for p1 in range(1, 5):
    for p2 in range (1, 5):
        for p3 in range(1, 5):
            for p4 in range(1, 5):
                for p5 in range(1, 5):
                    for p6 in range(1, 5):
                        for p7 in range(1, 5):
                            for p8 in range(1, 5):
                                for p9 in range(1, 5):
                                    pyramidal[p1+p2+p3+p4+p5+p6+p7+p8+p9] += 1

# obtain the number of ways to get each sum with 6 cubic dice
cubic = {}
for x in range(6, 37):
    cubic[x] = 0
for c1 in range(1, 7):
    for c2 in range(1, 7):
        for c3 in range(1, 7):
            for c4 in range(1, 7):
                for c5 in range(1, 7):
                    for c6 in range(1, 7):
                        cubic[c1+c2+c3+c4+c5+c6] += 1

total_games = sum(pyramidal.values()) * sum(cubic.values())
pyramidal_win = 0
for sum_pyramidal in pyramidal:
    for sum_cubic in cubic:
        if sum_pyramidal > sum_cubic:
            pyramidal_win += pyramidal[sum_pyramidal] * cubic[sum_cubic]

print(round(pyramidal_win / total_games, 7))

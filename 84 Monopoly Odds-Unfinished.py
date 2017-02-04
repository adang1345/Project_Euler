"""In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	                                C1
T2	 	                                U1
H1	 	                                C2
CH3	 	                                C3
R4	 	                                R2
G3	 	                                D1
CC3	 	                                CC2
G2	 	                                D2
G1	 	                                D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance
in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%.
However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player
rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to
jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from
the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There
are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a
movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL

Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing
at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to
another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall
make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a
double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to
produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit
modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string."""

from random import randint


def dice_roll():
    """Return the result from rolling two 6-sided dice as a tuple."""
    return randint(1, 6), randint(1, 6)


def final_square(initial_square, current_roll, last_2_rolls):
    """Return the final square where the player will end up, starting from an initial square and rolling the tuple
    roll_value. We are also given the results of the last 2 rolls. If any of these 2 rolls do not exist, then (7,8) is
    used as a placeholder."""

    # consider case where three doubles are rolled in a row
    if current_roll[0] == current_roll[1] and last_2_rolls[0][0] == last_2_rolls[0][1] and \
        last_2_rolls[1][0] == last_2_rolls[1][1]:
        return 10  # go to jail

    # go to the next square
    next_square = (initial_square + sum(current_roll)) % 40

    # 



squares = tuple(range(40))
square_counts = [0] * 40

init_square = 0
for _ in range(1000000):
    next_square = final_square(init_square, dice_roll())
    square_counts[next_square] += 1
    init_square = next_square

print(square_counts)

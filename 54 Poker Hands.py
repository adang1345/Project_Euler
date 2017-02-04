"""In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights
beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then
highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?"""

# For the following functions, the parameter <cards> represents a list of 5 strings. A list represents a poker hand.
# An example is ["8C", "TS", "KC", "9H", "4S"].

value_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def sorted_hand(cards):
    """Return a sorted version of cards. Sorting is done by card value."""
    values = []
    for card in cards:
        values.append(value_order.index(card[0]))
    values_and_cards = list(zip(values, cards))
    values_and_cards.sort()
    return [y for (x, y) in values_and_cards]


def values(cards):
    """Return a list containing values of cards."""
    return [x[0] for x in cards]


def highest_value(cards):
    """Return the highest value in sorted cards."""
    return values(cards)[-1]


def same_suits(cards):
    """Return True if cards are all same the same suit, False otherwise."""
    return len(set([x[1] for x in cards])) == 1


def is_royal_flush(cards):
    """Return True if sorted cards is a Royal Flush, False otherwise."""
    return values(cards) == ["T", "J", "Q", "K", "A"] and same_suits(cards)


def is_straight_flush(cards):
    """Return True if sorted cards is a Straight Flush, False otherwise."""
    card_values = values(cards)
    for x in range(1, 5):
        if value_order.index(card_values[x - 1]) + 1 != value_order.index(card_values[x]):
            return False
    return same_suits(cards)


def is_four_of_a_kind(cards):
    """Return True if cards is Four of a Kind."""
    card_values = values(cards)
    for card_value in value_order:
        if card_values.count(card_value) == 4:
            return True
    return False


def four_of_a_kind_score_addition(cards):
    """Return the fractional part of the score for a hand containing Four of a Kind."""
    s = 0
    scores = values(cards)
    for x in scores:
        if scores.count(x) == 4:
            s += value_order.index(x) / 100
            break
    for x in scores:
        if scores.count(x) == 1:
            s += value_order.index(x) / 10000
            break
    return s


def is_full_house(cards):
    """Return True if sorted cards is a Full House."""
    card_values = values(cards)
    lowest_value = card_values[0]
    highest_value = card_values[-1]
    return (card_values.count(lowest_value) == 3 and card_values.count(highest_value) == 2 or
            card_values.count(lowest_value) == 2 and card_values.count(highest_value) == 3)


def full_house_score_addition(cards):
    """Return the fractional part of the score for a hand containing a Full House."""
    s = 0
    scores = values(cards)
    for x in scores:
        if scores.count(x) == 3:
            s += value_order.index(x) / 100
            break
    for x in scores:
        if scores.count(x) == 2:
            s += value_order.index(x) / 10000
            break
    return s


def is_flush(cards):
    """Return True if cards is a Flush, False otherwise."""
    return same_suits(cards)


def flush_score_or_highest_card_addition(cards):
    """Return the fractional part of the score for a sorted hand containing a Flush or Highest Card."""
    s = 0
    v = values(cards)
    for x in range(len(v)):
        s += value_order.index(v[x]) / (10 ** (10 - 2*x))
    return s


def is_straight(cards):
    """Return True if sorted cards is Straight, False otherwise."""
    card_values = values(cards)
    for x in range(1, 5):
        if value_order.index(card_values[x - 1]) + 1 != value_order.index(card_values[x]):
            return False
    return True


def is_three_of_a_kind(cards):
    """Return True if cards is Three of a Kind."""
    card_values = values(cards)
    for card_value in value_order:
        if card_values.count(card_value) == 3:
            return True
    return False


def three_of_a_kind_score_addition(cards):
    """Return the fractional part of the score for a sorted hand containing a Three of a Kind."""
    s = 0
    v = values(cards)
    # Divide values into 2 lists. list1 contains the Three of a Kind; list2 contains the other 2 cards.
    list1 = []
    list2 = []
    for x in v:
        if v.count(x) == 3:
            list1.append(x)
        else:
            list2.append(x)
    assert len(list1) == 3 and len(list2) == 2
    # account for the card value of the three-of-a-kind
    s += value_order.index(list1[0]) / 100
    # account for the value of the larger non-three-of-a-kind card
    s += value_order.index(list2[1]) / 10000
    # account for the value of the smaller non-three-of-a-kind card
    s += value_order.index(list2[0]) / 1000000
    return s


def is_two_pairs(cards):
    """Return True if cards is Two Pairs."""
    return len(set(values(cards))) == 3


def two_pairs_score_addition(cards):
    """Return the fractional part of the score for a sorted hand containing Two Pairs."""
    s = 0
    v = values(cards)
    # Divide values into 2 lists. list1 contains the two pairs; list2 contains the other card.
    list1 = []
    list2 = []
    for x in v:
        if v.count(x) == 2:
            list1.append(x)
        else:
            list2.append(x)
    assert len(list1) == 4 and len(list2) == 1
    # account for the card value of the higher pair
    s += value_order.index(list1[-1]) / 100
    # account for the card value of the lower pair
    s += value_order.index(list1[0]) / 10000
    # account for the value of the other card
    s += value_order.index(list2[0]) / 1000000
    return s


def is_one_pair(cards):
    """Return True if cards is One Pair."""
    return len(set(values(cards))) == 4


def one_pair_score_addition(cards):
    """Return the fractional part of the score for a sorted hand containing One Pair."""
    s = 0
    v = values(cards)
    # Divide values into 2 lists. list1 contains the pairs; list2 contains the other card.
    list1 = []
    list2 = []
    for x in v:
        if v.count(x) == 2:
            list1.append(x)
        else:
            list2.append(x)
    assert len(list1) == 2 and len(list2) == 3
    # account for the card value of the pair
    s += value_order.index(list1[0]) / 100
    # account for the card values of the other cards
    for x in range(len(list2)):
        s += value_order.index(list2[x]) / (10 ** (8 - 2*x))
    return s


def score(cards):
    """Generate a score for cards. A hand with a higher score beats a hand with a lower score."""
    cards = sorted_hand(cards)
    if is_royal_flush(cards):
        s = 9
    elif is_straight_flush(cards):
        s = 8 + value_order.index(highest_value(cards)) / 100
    elif is_four_of_a_kind(cards):
        s = 7 + four_of_a_kind_score_addition(cards)
    elif is_full_house(cards):
        s = 6 + full_house_score_addition(cards)
    elif is_flush(cards):
        s = 5 + flush_score_or_highest_card_addition(cards)
    elif is_straight(cards):
        s = 4 + value_order.index(highest_value(cards)) / 100
    elif is_three_of_a_kind(cards):
        s = 3 + three_of_a_kind_score_addition(cards)
    elif is_two_pairs(cards):
        s = 2 + two_pairs_score_addition(cards)
    elif is_one_pair(cards):
        s = 1 + one_pair_score_addition(cards)
    else:
        s = flush_score_or_highest_card_addition(cards)
    return s


count = 0
f = open("54 Poker.txt")
for line in f:
    hands = line.split()
    player_1_score = score(hands[:5])
    player_2_score = score(hands[5:])
    assert player_1_score != player_2_score
    if player_1_score > player_2_score:
        count += 1
f.close()

print(count)

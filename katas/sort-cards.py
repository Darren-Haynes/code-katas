"""Kata: Sort Deck of Cards - Write a function sort_cards() that sorts a
shuffled list of cards, so that any given list of cards is sorted by rank,
no matter the starting collection.

#1 Best Practices Solution by zebulan, Unnamed, acaccia, j_codez, Mr.Child,
iamchingel (plus 8 more warriors).

def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
"""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """

    nums = []
    alphas = []
    for card in cards:
        if card.isalpha():
            alphas.append(card)
        else:
            nums.append(card)

    nums.sort()

    for _ in range(alphas.count('A')):
        nums.insert(0, 'A')
    for _ in range(alphas.count('T')):
        nums.append('T')
    for _ in range(alphas.count('J')):
        nums.append('J')
    for _ in range(alphas.count('Q')):
        nums.append('Q')
    for _ in range(alphas.count('K')):
        nums.append('K')

    return nums

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
print(Card._fields)

class FrechDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    @staticmethod
    def spades_high(card):
        rank_value = FrechDeck.ranks.index(card.rank)
        return rank_value * len(FrechDeck.suit_values) + FrechDeck.suit_values[card.suit]

import random
from random import choice

if __name__ == '__main__':
    deck = FrechDeck()
    print(len(deck))

    print(choice(deck))

    for card in deck:
        print(card)

    print(Card('2', 'hearts') in deck)

    # for card in sorted(deck, key=FrechDeck.spades_high):
    #     print(card)

    random.shuffle(deck)
    for card in deck:
        print(card)

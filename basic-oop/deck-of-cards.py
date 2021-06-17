"""Data structures for a generic deck of cards"""
import random
from enum import Enum


class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

    def __str__(self):
        return self.name


class Card:
    def __init__(self, value: int, suit: Suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        map_letters = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        value_str = map_letters.get(self.value, self.value)
        return f'{value_str} {self.suit}'


class Deck:
    def __init__(self):
        self.size = 52
        self.cards = [Card(val, suit) for val in range(1, 14) for suit in Suit]

    def draw(self):
        if self.cards:
            self.size -= 1
            return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return str([str(card) for card in self.cards])


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def score(self):
        score = 0
        for card in self.cards:
            score += card.value

    def __str__(self):
        return str([str(card) for card in self.cards])


if __name__ == "__main__":
    my_deck = Deck()
    print(my_deck)
    my_deck.shuffle()
    print(my_deck)


from functools import total_ordering
from itertools import combinations

from Poker.models.CompareHandsFuncs import compare_hands


@total_ordering
class Card:
    value = 0
    suit = ''

    def __init__(self, card_value, suit):
        self.value = card_value
        self.suit = suit

    def __str__(self):
        if self.value == 1:
            return f"Ace of {self.suit}"
        elif self.value == 11:
            return f"Jack of {self.suit}"
        elif self.value == 12:
            return f"Queen of {self.suit}"
        elif self.value == 13:
            return f"King of {self.suit}"
        else:
            return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if type(other) == Card:
            return self.value == other.value
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(other) == Card:
            return self.value < other.value
        else:
            return NotImplemented


class Hand:
    hand = list()
    first_cards = list()

    def __init__(self, card1, card2, *args):
        self.hand = list()
        self.hand.append(card1)
        self.hand.append(card2)
        self.first_cards = list()
        self.first_cards.append(card1)
        self.first_cards.append(card2)
        for arg in args:
            self.hand.append(arg)

    def __str__(self):
        string = ''
        for card in self.hand:
            if string != '':
                string = f'{string}, {card}'
            else:
                string = f'{card}'
        return string

    def get_two_cards(self):
        return_string = str(self.first_cards[0])
        return_string = f'{return_string}<br>{self.first_cards[1]}'
        return return_string

    def addCard(self, card):
        self.hand.append(card)

    def setBestHand(self):
        # assuming more than 5 cards hand, get all 5 cards hand and decides the best one
        all_hands = list(combinations(self.hand, 5))  # all hands
        all_hands = list(map(list, all_hands))  # make all hands lists
        all_hands = list(map(sorted, all_hands))  # make all hands sorted
        best_hand = all_hands[0]
        for var_hand in all_hands[1:]:
            best_hand = var_hand if compare_hands(best_hand, var_hand) == var_hand else best_hand
        self.hand = best_hand

    def this_hand(self):
        self.hand.sort()
        return self.hand

    def __getitem__(self, item):
        return self.hand[item]

    def __setitem__(self, key, value):
        self.hand[key] = value


class Deck:
    cards_list = list()

    def __init__(self):
        self.cards_list.clear()
        for value in range(1, 14):
            for suit in ('diamonds', 'clubs', 'hearts', 'spades'):
                self.cards_list.append(Card(value, suit))

    def __str__(self):
        string = ""
        for i in self.cards_list:
            string += f"{i}\n"
        return string

    def __getitem__(self, item):
        return self.cards_list[item]

    def __setitem__(self, key, value):
        self.cards_list[key] = value

    def get_n_cards(self, n):
        n_cards = list()
        for _ in range(n):
            n_cards.append(self.cards_list.pop())
        return n_cards

    def addCard(self, card, *args):
        self.cards_list.append(card)
        for other_card in args:
            self.cards_list.append(other_card)

    def pop(self, index=0):
        return self.cards_list.pop(index)


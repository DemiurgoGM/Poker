import itertools

from Poker.models.Deck import compare_hands


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
        # assuming 7 cards hand, get all 5 cards hand and decides the best one
        all_hands = list(itertools.combinations(self.hand, 5))
        best_hand = all_hands[0]
        for var_hand in all_hands[1:]:
            best_hand = var_hand if compare_hands(best_hand, var_hand) == var_hand else best_hand
        self.hand = best_hand


class Player:
    user = ''
    money = 0

    def __init__(self, username, value):
        self.user = username
        self.money = value

    def __str__(self):
        return f'{self.user} has ${self.money}'

# hand = Hand(Card(8, 'a'), Card(4, 'a'), Card(2, 'd'), Card(3, 'b'), Card(6, 'e'), Card(11, 'c'), Card(13, 'd'))
# hand.setBestHand()
# print(hand)

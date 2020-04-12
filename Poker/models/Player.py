
class Hand:
    hand = []

    def __init__(self, card1, card2):
        self.hand = [card1, card2]

    def __str__(self):
        string = ''
        for card in self.hand:
            if string != '':
                string = f'{string}; {card}'
            else:
                string = f'{card}'
        return string


class Player:
    user = ''
    money = 0
    hand = []

    def __init__(self, username, value, hand=None):
        self.user = username
        self.money = value
        self.hand = hand

    def __str__(self):
        return f'{self.user} has ${self.money} with the hand {self.hand}'


# hand = Hand(Card(1, 'a'), Card(2, 'a'))
# print(hand)

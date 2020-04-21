
class Hand:
    hand = list()

    def __init__(self, card1, card2):
        self.hand = list()
        self.hand.append(card1)
        self.hand.append(card2)

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

    def __init__(self, username, value):
        self.user = username
        self.money = value

    def __str__(self):
        return f'{self.user} has ${self.money}'

# hand = Hand(Card(1, 'a'), Card(2, 'a'))
# print(hand)

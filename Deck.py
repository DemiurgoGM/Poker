class Card:
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


class Deck:
    def __init__(self):
        self.cards_list = list()
        for value in range(1, 14):
            for suit in ('diamonds', 'clubs', 'hearts', 'spades'):
                self.cards_list.append(Card(value, suit))

    def __str__(self):
        string = ""
        for i in self.cards_list:
            string += f"{i}\n"
        return string


def getKicker(hand):
    first_card = hand[0]
    if first_card.value == 1:  # The plan is to get the hand ordered
        return 14
    new_hand = hand[0:1]
    for card in new_hand:
        if card.value > first_card.value:
            first_card = card
    return first_card.value


def isStaightFlush(hand):
    first_card = hand[0]
    new_hand = hand[1:]
    counter = 0
    for card in new_hand:  # The plan is to get the hand ordered
        if (card.value == first_card.value + 1 or (card.value == 1 and first_card.value == 13)) \
                and card.suit == first_card.suit:
            first_card = card
            counter = counter + 1
            continue
        else:
            break
    return counter == 5


def isQuad(hand):
    counter = 0
    first_card = hand[0]
    new_hand = hand[1:]
    for card in new_hand:
        if card.value == first_card:
            counter = counter + 1
            first_card = card
            continue

    return counter == 3


def compare_hands(hand_one, hand_two):
    if isStaightFlush(hand_one):
        if isStaightFlush(hand_two):
            if getKicker(hand_one) > getKicker(hand_two):
                return hand_one
            elif getKicker(hand_one) < getKicker(hand_two):
                return hand_two
            else:
                return list()  # Draw = empty list
        else:
            return hand_one
    elif isStaightFlush(hand_two):
        return hand_two
    elif isQuad(hand_one):
        if isQuad(hand_two):
            pass  # TODO
    elif isFullHouse(hand_one):
        pass
    elif isFlush(hand_one):
        pass
    elif isStraight(hand_one):
        pass
    elif isThreeEquals(hand_one):
        pass
    elif isTwoPair(hand_one):
        pass
    elif isPair(hand_one):
        pass
    else:  # Bigger kicker wins
        pass

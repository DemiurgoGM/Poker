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
    if hand[0].value == 1 or hand[-1].value == 1:
        return 14
    first_card = hand[0]
    for card in hand[1:]:
        if card.value > first_card.value:
            first_card = card
    return first_card.value


def isStaightFlush(hand):
    first_card = hand[0]
    counter = 0
    for card in hand[1:]:  # The plan is to get the hand ordered
        if (card.value == first_card.value + 1 or (card.value == 1 and first_card.value == 13)) \
                and card.suit == first_card.suit:
            first_card = card
            counter = counter + 1
            continue
        else:
            break
    return counter == 4


def isQuad(hand):
    counter = 0
    first_card = hand[0]
    for card in hand[1:]:
        if card.value == first_card.value:
            counter = counter + 1
            continue

    return counter == 3


def getQuadKicker(hand):
    if isQuad(hand):
        value = hand[-1].value
        if value == 1:
            return 14
        else:
            return value
    else:
        return -1


def getQuadCard(hand):
    if isQuad(hand):
        value = hand[0].value
        if value == 1:
            return 14
        else:
            return value
    else:
        return -1


def isFullHouse(hand):
    cards_value = list()
    for card in hand:
        cards_value.append(card.value)
    return cards_value.count(cards_value[0]) == 3 and cards_value.count(cards_value[-1]) == 2


def getFullHouseThreeCard(hand):
    if isFullHouse(hand):
        value = hand[0].value
        if value == 1:
            return 14
        else:
            return value
    else:
        return -1


def getFullHouseTwoCard(hand):
    if isFullHouse(hand):
        value = hand[-1].value
        if value == 1:
            return 14
        else:
            return value
    else:
        return -1


def isFlush(hand):
    counter = 0
    first_card = hand[0]
    for card in hand[1:]:
        if card.suit == first_card.suit:
            counter = counter + 1
        else:
            break
    return counter == 4


def isStraight(hand):
    first_card = hand[0]
    counter = 0
    for card in hand[1:]:  # The plan is to get the hand ordered
        if card.value == first_card.value + 1 or (card.value == 1 and first_card.value == 13):
            first_card = card
            counter = counter + 1
        else:
            break
    return counter == 4


def isThreeEquals(hand_one):
    pass


def isTwoPair(hand_one):
    pass


def isPair(hand_one):
    pass


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
    elif isQuad(hand_one):  # if quad
        if isQuad(hand_two):  # if 2 quads
            if getQuadCard(hand_one) == getQuadCard(hand_two):  # if same quad
                if getQuadKicker(hand_one) > getQuadKicker(hand_two):
                    return hand_one
                elif getQuadKicker(hand_two) > getQuadKicker(hand_one):
                    return hand_two
                else:
                    return list()
            elif getQuadCard(hand_one) > getQuadCard(hand_two):
                return hand_one
            else:
                return hand_two
        else:
            return hand_one
    elif isQuad(hand_two):
        return hand_two
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
        if getKicker(hand_one) > getKicker(hand_two):
            return hand_one
        elif getKicker(hand_one) < getKicker(hand_two):
            return hand_two
        else:
            return list()  # Draw = empty list


# hand = (Card(5, 'a'), Card(3, 'a'), Card(7, 'a'), Card(8, 'a'), Card(9, 'a'))
# print(isStraight(hand))

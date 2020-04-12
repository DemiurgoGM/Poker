
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


class Deck:
    cards_list = list()

    def __init__(self):
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


# def isStraightWorkingTest(hand):  # if the hand received isn't ordered, use this instead
#     counter = 0
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     if cards_value[0] == 1 and cards_value[-1] == 13:
#         cards_value[0] = 14
#         cards_value.sort()
#     first_value = cards_value[0]
#     for value in cards_value[1:]:
#         if value == first_value + 1:
#             counter = counter + 1
#             first_value = value
#     return counter == 4


def isThreeEquals(hand):
    counter = 0
    first_card = hand[0]
    for card in hand[1:]:
        if card.value == first_card.value:
            counter = counter + 1
    return counter == 2


def getThreeEqualCard(hand):
    cards_value = list()
    for card in hand:
        cards_value.append(card.value)
    cards_value.sort()
    for i in range(1, 14):
        if cards_value.count(i) == 3:
            return 14 if i == 1 else i
    return -1  # didn't find the repeating card.


def getNotRepeatedHand(hand):
    cards_value = list()
    for card in hand:
        cards_value.append(card.value)
    for i in range(1, 14):
        if cards_value.count(i) > 1:
            while cards_value.count(i) > 0:
                cards_value.remove(i)
    return cards_value


def isTwoPair(hand):
    cards_value = list()
    for card in hand:
        cards_value.append(card.value)
    return cards_value.count(cards_value[0]) == 2 and cards_value.count(cards_value[2]) == 2


def getBiggerValueFromPairedHand(hand):
    cards_value = list()
    pair_values = list()
    for card in hand:
        cards_value.append(card.value)
    while cards_value.count(1) > 0:
        cards_value.remove(1)
        cards_value.append(14)
    for i in range(2, 15):
        if cards_value.count(i) > 1:
            pair_values.append(i)
    return max(pair_values)


def getSmallerValueFromPairedHand(hand):
    cards_value = list()
    pair_values = list()
    for card in hand:
        cards_value.append(card.value)
    while cards_value.count(1) > 0:
        cards_value.remove(1)
        cards_value.append(14)
    for i in range(1, 14):
        if cards_value.count(i) > 1:
            pair_values.append(i)
    return min(pair_values)


def isPair(hand):
    cards_value = list()
    for card in hand:
        cards_value.append(card.value)
    for i in range(0, 5):
        if cards_value.count(cards_value[i]) == 2:
            return True
    return False


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
        if isFullHouse(hand_two):  # if both full houses
            if getFullHouseThreeCard(hand_one) > getFullHouseThreeCard(hand_two):  # bigger three card wins
                return hand_one
            elif getFullHouseThreeCard(hand_two) > getFullHouseThreeCard(hand_one):
                return hand_two
            elif getFullHouseTwoCard(hand_one) > getFullHouseTwoCard(hand_two):
                # if both same three-card, bigger two card wins
                return hand_one
            elif getFullHouseTwoCard(hand_two) > getFullHouseTwoCard(hand_one):
                return hand_two
            else:
                return list()
        else:
            return hand_one
    elif isFullHouse(hand_two):
        return hand_two
    elif isFlush(hand_one):
        if isFlush(hand_two):
            if getKicker(hand_one) > getKicker(hand_two):
                return hand_one
            elif getKicker(hand_two) > getKicker(hand_one):
                return hand_two
            else:
                return list()
        else:
            return hand_one
    elif isFlush(hand_two):
        return hand_two
    elif isStraight(hand_one):
        if isStraight(hand_two):
            if getKicker(hand_one) > getKicker(hand_two):
                return hand_one
            elif getKicker(hand_two) > getKicker(hand_one):
                return hand_two
            else:
                return list()
        else:
            return hand_one
    elif isStraight(hand_two):
        return hand_two
    elif isThreeEquals(hand_one):
        if isThreeEquals(hand_two):
            if getThreeEqualCard(hand_one) > getThreeEqualCard(hand_two):
                return hand_one
            elif getThreeEqualCard(hand_two) > getThreeEqualCard(hand_one):
                return hand_two
            else:
                hand_one_cards = getNotRepeatedHand(hand_one)
                hand_two_cards = getNotRepeatedHand(hand_two)
                if hand_one_cards.count(1) > 0:
                    hand_one_cards[hand_one_cards.index(1)] = 14
                if hand_two_cards.count(1) > 0:
                    hand_two_cards[hand_two_cards.index(1)] = 14
                hand_one_cards.sort()
                hand_two_cards.sort()
                for i in range(3, -1, -1):
                    if hand_one_cards[i] > hand_two_cards[i]:
                        return hand_one
                    elif hand_two_cards[i] > hand_one_cards[i]:
                        return hand_two
                return list()
        else:
            return hand_one
    elif isThreeEquals(hand_two):
        return hand_two
    elif isTwoPair(hand_one):
        if isTwoPair(hand_two):
            hand_one_big_value = getBiggerValueFromPairedHand(hand_one)
            hand_two_big_value = getSmallerValueFromPairedHand(hand_two)
            if hand_one_big_value > hand_two_big_value:
                return hand_one
            elif hand_two_big_value > hand_one_big_value:
                return hand_two
            else:
                hand_one_small_value = getSmallerValueFromPairedHand(hand_one)
                hand_two_small_value = getSmallerValueFromPairedHand(hand_two)
                if hand_one_small_value > hand_two_small_value:
                    return hand_one
                elif hand_two_small_value > hand_one_small_value:
                    return hand_two
                else:
                    hand_one_unrepeated = getNotRepeatedHand(hand_one)[0]
                    hand_two_unrepeated = getNotRepeatedHand(hand_two)[0]
                    if hand_one_unrepeated > hand_two_unrepeated:
                        return hand_one
                    elif hand_two_unrepeated > hand_one_unrepeated:
                        return hand_two
                    else:
                        list()
        else:
            return hand_one
    elif isTwoPair(hand_two):
        return hand_two
    elif isPair(hand_one):
        if isPair(hand_two):
            hand_one_pair_value = getBiggerValueFromPairedHand(hand_one)
            hand_two_pair_value = getBiggerValueFromPairedHand(hand_two)
            if hand_one_pair_value > hand_two_pair_value:
                return hand_one
            elif hand_two_pair_value > hand_one_pair_value:
                return hand_two
            else:
                hand_one_unrepeated = getNotRepeatedHand(hand_one)
                hand_two_unrepeated = getNotRepeatedHand(hand_two)
                while hand_one_unrepeated.count(1) > 0:
                    hand_one_unrepeated.remove(1)
                    hand_one_unrepeated.append(14)
                while hand_two_unrepeated.count(1) > 0:
                    hand_two_unrepeated.remove(1)
                    hand_two_unrepeated.append(14)
                hand_one_unrepeated.sort()
                hand_two_unrepeated.sort()
                for i in range(2, -1, -1):
                    if hand_one_unrepeated[i] > hand_two_unrepeated[i]:
                        return hand_one
                    elif hand_two_unrepeated[i] > hand_one_unrepeated[i]:
                        return hand_two
                return list()
        else:
            return hand_one
    elif isPair(hand_two):
        return hand_two
    else:  # Bigger kicker wins, if equals see other big card...
        first_hand_cards = list()
        second_hand_cards = list()
        for card in hand_one:
            first_hand_cards.append(card.value)
        for card in hand_two:
            second_hand_cards.append(card.value)
        first_hand_cards.sort()
        if first_hand_cards[0] == 1:
            first_hand_cards[0] = 14
            first_hand_cards.sort()
        second_hand_cards.sort()
        if second_hand_cards[0] == 1:
            second_hand_cards[0] = 14
            second_hand_cards.sort()
        for i in range(4, -1, -1):
            if first_hand_cards[i] > second_hand_cards[i]:
                return hand_one
            elif second_hand_cards[i] > first_hand_cards[i]:
                return hand_two
        return list()

# hand = (Card(1, 'a'), Card(2, 'a'), Card(13, 'a'), Card(2, 'a'), Card(3, 'a'))
# print(getNotRepeatedHand(hand))

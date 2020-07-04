
def isStaightFlush(hand):
    return isStraight(hand) and isFlush(hand)


def isQuad(hand):  # if the hand received is ordered, use this
    return hand.count(hand[0]) == 4 or hand.count(hand[-1]) == 4


# def isQuad(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for i in range(2):
#         if cards_value.count(cards_value[i]) == 4:
#             return True
#     return False


def getQuadKicker(hand):  # if the hand received is ordered, use this
    value = -1
    if hand.count(hand[0]) == 4:
        value = hand[-1]
    elif hand.count(hand[-1]) == 4:
        value = hand[0]
    return 14 if value == 1 else value


# def getQuadKicker(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 4:
#         value = cards_value[-1]
#     elif cards_value.count(cards_value[-1]) == 4:
#         value = cards_value[0]
#     return 14 if value == 1 else value


def getQuadCard(hand):  # if the hand received is ordered, use this
    value = -1
    if hand.count(hand[0]) == 4:
        value = hand[0]
    elif hand.count(hand[-1]) == 4:
        value = hand[-1]
    return 14 if value == 1 else value


# def getQuadCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 4:
#         value = cards_value[0]
#     elif cards_value.count(cards_value[-1]) == 4:
#         value = cards_value[-1]
#     return 14 if value == 1 else value


def isFullHouse(hand):  # if the hand received is ordered, use this
    return (hand.count(hand[0]) == 3 and hand.count(hand[-1]) == 2) or \
           (hand.count(hand[0]) == 2 and hand.count(hand[-1]) == 3)


# def isFullHouse(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     return (cards_value.count(cards_value[0]) == 3 and cards_value.count(cards_value[-1]) == 2) or \
#            (cards_value.count(cards_value[0]) == 2 and cards_value.count(cards_value[-1]) == 3)


def getFullHouseThreeCard(hand):  # if the hand received is ordered, use this
    value = -1
    if hand.count(hand[0]) == 3:
        value = hand[0]
    elif hand.count(hand[-1]) == 3:
        value = hand[-1]
    return 14 if value == 1 else value


# def getFullHouseThreeCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 3:
#         value = cards_value[0]
#     elif cards_value.count(cards_value[-1]) == 3:
#         value = cards_value[-1]
#     return 14 if value == 1 else value


def getFullHouseTwoCard(hand):  # if the hand received is ordered, use this
    value = -1
    if hand.count(hand[0]) == 2:
        value = hand[0]
    elif hand.count(hand[-1]) == 2:
        value = hand[-1]
    return 14 if value == 1 else value


# def getFullHouseTwoCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 2:
#         value = cards_value[0]
#     elif cards_value.count(cards_value[-1]) == 2:
#         value = cards_value[-1]
#     return 14 if value == 1 else value


def isFlush(hand):
    counter = 0
    first_card = hand[0]
    for card in hand[1:]:
        if card.suit == first_card.suit:
            counter = counter + 1
        else:
            return False
    return counter == 4


def isStraight(hand):  # if the hand received is ordered, use this
    counter = 0
    first_card_value = hand[0].value
    for card in hand[1:]:
        if card.value == first_card_value + 1 or \
                (card.value == 13 and hand[0].value == 1) or \
                (card.value == 10 and first_card_value == 1):
            counter = counter + 1
        first_card_value = card.value
    return counter == 4


# def isStraight(hand):  # if the hand received isn't ordered, use this instead
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


def isThreeEquals(hand):  # if the hand received is ordered, use this
    for i in range(3):
        if hand.count(hand[i]) == 3:
            return True
    return False


# def isThreeEquals(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for i in range(3):
#         if cards_value.count(cards_value[i]) == 3:
#             return True
#     return False


def getThreeEqualCard(hand):  # if the hand received is ordered, use this
    for i in range(3):
        if hand.count(hand[i]) == 3:
            return hand[i] if hand[i] != 1 else 14
    return -1  # didn't find the repeating card.


# def getThreeEqualCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for i in range(3):
#         if cards_value.count(cards_value[i]) == 3:
#             return cards_value[i] if cards_value[i] != 1 else 14
#     return -1  # didn't find the repeating card.


def getNotRepeatedHandValues(hand):
    cards_value = list()
    for card in hand:
        cards_value.append(card.value)
    for value in cards_value:
        if cards_value.count(value) > 1:
            while cards_value.count(value) > 0:
                cards_value.remove(value)
    cards_value.sort()
    return cards_value


def isTwoPair(hand):  # if the hand received is ordered, use this
    counter = 0
    for card in hand[::2]:
        if hand.count(card) == 2:
            counter = counter + 1
    return counter == 2


# def isTwoPair(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     counter = 0
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for value in cards_value:
#         if cards_value.count(value) == 2:
#             counter = counter + 1
#             cards_value.remove(value)
#     return counter == 2


def getBiggerValueFromPairedHand(hand):  # if the hand received is ordered, use this
    pair_values = list()
    for card in hand[::2]:
        if hand.count(card) == 2:
            pair_values.append(14 if card.value == 1 else card.value)
    return max(pair_values)


# def getBiggerValueFromPairedHand(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     pair_values = list()
#     for card in hand:
#         cards_value.append(card.value)
#     while cards_value.count(1) > 0:
#         cards_value.remove(1)
#         cards_value.append(14)
#     for i in range(2, 15):
#         if cards_value.count(i) > 1:
#             pair_values.append(i)
#     return max(pair_values)


def getSmallerValueFromPairedHand(hand):  # if the hand received is ordered, use this
    pair_values = list()
    for card in hand[::2]:
        if hand.count(card) == 2:
            pair_values.append(14 if card.value == 1 else card.value)
    return min(pair_values)


# def getSmallerValueFromPairedHand(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     pair_values = list()
#     for card in hand:
#         cards_value.append(card.value)
#     while cards_value.count(1) > 0:
#         cards_value.remove(1)
#         cards_value.append(14)
#     for i in range(1, 14):
#         if cards_value.count(i) > 1:
#             pair_values.append(i)
#     return min(pair_values)


def isPair(hand):  # if the hand received is ordered, use this
    for card in hand[::2]:
        if hand.count(card) == 2:
            return True
    return False


# def isPair(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     for i in range(4):
#         if cards_value.count(cards_value[i]) == 2:
#             return True
#     return False


# def getKicker(hand):  # if the hand received is ordered, use this
#     return 14 if hand[0] == 1 else hand[-1]


# def getKicker(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     return 14 if cards_value[0] == 1 else cards_value[-1]


def compare_hands_values(hand_one, hand_two):  # assuming all different cards
    # if the hand received is ordered, use this
    if hand_one[0].value == 1 and hand_two[0].value != 1:
        return hand_one
    elif hand_one[0].value != 1 and hand_two[0].value == 1:
        return hand_two
    else:
        for i in range(4, -1, -1):
            if hand_one[i].value > hand_two[i].value:
                return hand_one
            elif hand_two[i].value > hand_one[i].value:
                return hand_two
    return list()


# def compare_hands_values(hand_one, hand_two):  # assuming all different cards
#     # if the hand received isn't ordered, use this
#     first_hand_cards = list()
#     second_hand_cards = list()
#     for card in hand_one:
#         first_hand_cards.append(card.value)
#     for card in hand_two:
#         second_hand_cards.append(card.value)
#     first_hand_cards.sort()
#     if first_hand_cards[0] == 1:
#         first_hand_cards[0] = 14
#         first_hand_cards.sort()
#     second_hand_cards.sort()
#     if second_hand_cards[0] == 1:
#         second_hand_cards[0] = 14
#         second_hand_cards.sort()
#     for i in range(4, -1, -1):
#         if first_hand_cards[i] > second_hand_cards[i]:
#             return hand_one
#         elif second_hand_cards[i] > first_hand_cards[i]:
#             return hand_two
#     return list()


def compare_hands(hand_one, hand_two):
    hand_one = list(hand_one)
    hand_two = list(hand_two)
    hand_one.sort()
    hand_two.sort()
    if isStaightFlush(hand_one):
        if isStaightFlush(hand_two):
            return compare_hands_values(hand_one, hand_two)
        else:
            return hand_one
    elif isStaightFlush(hand_two):
        return hand_two
    elif isQuad(hand_one):  # if quad
        if isQuad(hand_two):  # if 2 quads
            hand_one_quad_card = getQuadCard(hand_one)
            hand_two_quad_card = getQuadCard(hand_two)
            if hand_one_quad_card == hand_two_quad_card:  # if same quad
                hand_one_quad_kicker = getQuadKicker(hand_one)
                hand_two_quad_kicker = getQuadKicker(hand_two)
                if hand_one_quad_kicker > hand_two_quad_kicker:
                    return hand_one
                elif hand_two_quad_kicker > hand_one_quad_kicker:
                    return hand_two
                else:
                    return list()
            elif hand_one_quad_card > hand_two_quad_card:
                return hand_one
            else:
                return hand_two
        else:
            return hand_one
    elif isQuad(hand_two):
        return hand_two
    elif isFullHouse(hand_one):
        if isFullHouse(hand_two):  # if both full houses
            hand_one_three_card = getFullHouseThreeCard(hand_one)
            hand_two_three_card = getFullHouseThreeCard(hand_two)
            if hand_one_three_card > hand_two_three_card:  # bigger three card wins
                return hand_one
            elif hand_two_three_card > hand_one_three_card:
                return hand_two

            hand_one_two_card = getFullHouseTwoCard(hand_one)
            hand_two_two_card = getFullHouseTwoCard(hand_two)
            if hand_one_two_card > hand_two_two_card:
                # if both same three-card, bigger two card wins
                return hand_one
            elif hand_two_two_card > hand_one_two_card:
                return hand_two
            else:
                return list()
        else:
            return hand_one
    elif isFullHouse(hand_two):
        return hand_two
    elif isFlush(hand_one):
        if isFlush(hand_two):
            return compare_hands_values(hand_one, hand_two)
        else:
            return hand_one
    elif isFlush(hand_two):
        return hand_two
    elif isStraight(hand_one):
        if isStraight(hand_two):
            return compare_hands_values(hand_one, hand_two)
        else:
            return hand_one
    elif isStraight(hand_two):
        return hand_two
    elif isThreeEquals(hand_one):
        if isThreeEquals(hand_two):
            hand_one_three_card = getThreeEqualCard(hand_one)
            hand_two_three_card = getThreeEqualCard(hand_two)
            if hand_one_three_card > hand_two_three_card:
                return hand_one
            elif hand_two_three_card > hand_one_three_card:
                return hand_two
            else:
                hand_one_cards = getNotRepeatedHandValues(hand_one)
                hand_two_cards = getNotRepeatedHandValues(hand_two)
                if hand_one_cards.count(1) > 0:
                    hand_one_cards[hand_one_cards.index(1)] = 14
                if hand_two_cards.count(1) > 0:
                    hand_two_cards[hand_two_cards.index(1)] = 14
                hand_one_cards.sort()
                hand_two_cards.sort()
                for i in range(1, -1, -1):
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
            hand_two_big_value = getBiggerValueFromPairedHand(hand_two)
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
                    hand_one_unrepeated = getNotRepeatedHandValues(hand_one)[0]
                    hand_two_unrepeated = getNotRepeatedHandValues(hand_two)[0]
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
                hand_one_unrepeated = getNotRepeatedHandValues(hand_one)
                hand_two_unrepeated = getNotRepeatedHandValues(hand_two)
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
        return compare_hands_values(hand_one, hand_two)


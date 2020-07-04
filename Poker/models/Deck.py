
import functools
import itertools

from Poker.models.HandComparingFunc import *


@functools.total_ordering
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
        all_hands = list(itertools.combinations(self.hand, 5))
        best_hand = all_hands[0]
        for var_hand in all_hands[1:]:
            best_hand = var_hand if compare_hands(best_hand, var_hand) == var_hand else best_hand
        self.hand = best_hand


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
        for i in range(n):
            n_cards.append(self.cards_list[-n - i])
        return n_cards


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


# hand = [Card(2, 'a'), Card(2, 'b'), Card(9, 'a'), Card(3, 'a'), Card(1, 'a')]
# hand2 = [Card(2, 'a'), Card(2, 'b'), Card(4, 'a'), Card(3, 'a'), Card(1, 'a')]
# print(compare_hands(hand, hand2))

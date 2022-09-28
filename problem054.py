# Long problem so for reference: https://projecteuler.net/problem=54
# Manipulated input file by adding a newline to the end of the file.
from collections import Counter


class Card:
    def __init__(self, number, suit):
        numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
                   'Q': 12, 'K': 13, 'A': 14}
        self.number = numbers[number]
        self.suit = suit


class Hand:
    def __init__(self, cards):
        self.cards = []
        self.suits = []
        self.numbers = []
        self.hc = 0
        self.value = 1
        self.token = 0
        self.kind = "high card"
        for card in cards:
            self.cards.append(Card(card[0], card[1]))

    def print_cards(self):
        for card in self.cards:
            print(card.number, card.suit)

    def calculate_value(self):
        for card in self.cards:
            self.suits.append(card.suit)
            self.numbers.append(card.number)
        self.numbers.sort()
        # Check if we have straight
        if self.numbers == list(range(min(self.numbers), max(self.numbers)+1)):
            self.kind = 'straight'
            self.value = 5
            self.token = max(self.numbers)
        # Check if flush
        if len(set(self.suits)) == 1:
            self.token = max(self.numbers)
            # Check if straight flush
            if self.kind == 'straight':
                self.kind = 'straight flush'
                self.value = 9
                # Check if royal flush
                if sum(self.numbers) == 60:
                    self.value = 10
                    self.kind = 'royal flush'
            else:
                self.kind = 'flush'
                self.value = 6
        # Check four of a kind
        counts = Counter(self.numbers)
        counts = counts.most_common()
        for c in counts:
            if c[1] == 4:
                self.value = 8
                self.kind = 'four of a kind'
                self.token = c[0]
            if c[1] == 3:
                self.value = 4
                self.kind = 'three of a kind'
                self.token = c[0]
            if c[1] == 2:
                if self.value == 4:
                    self.value = 7
                    self.kind = 'full house'
                elif self.value == 2:
                    self.value = 3
                    self.kind = 'two pair'
                    self.token = max(self.token, c[0])
                else:
                    self.value = 2
                    self.kind = 'one pair'
                    self.token = c[0]

    def calculate_hc(self, nignore=0):
        numbers_ = sorted(self.numbers, reverse=True)
        self.hc = max(numbers_[nignore:])


hands1 = []
hands2 = []

with open("input_data/problem054_input.txt", "r") as f:
    for line in f:
        hands1.append(line[0:14].split(' '))
        hands2.append(line[15:-1].split(' '))

nwins = 0
j = 1
for h1, h2 in zip(hands1, hands2):
    print(j)
    # print(h1)
    print(h2)
    hand1 = Hand(h1)
    hand2 = Hand(h2)
    hand1.calculate_value()
    hand2.calculate_value()
    # print(hand1.kind, hand2.kind)
    if hand1.value > hand2.value:
        nwins += 1
        # print('Player 1 wins')
    elif hand1.value == hand2.value:
        # print('Highest value')
        # print(hand1.token, hand2.token)
        hand1.calculate_hc()
        hand2.calculate_hc()
        if hand1.token > hand2.token:
            nwins += 1
            # print('Player 1 wins')
        elif hand1.token == hand2.token:
            # print('High card')
            # print(hand1.hc, hand2.hc)
            if hand1.hc > hand2.hc:
                nwins += 1
                # print('Player 1 wins')
            elif hand1.hc == hand2.hc:
                i = 1
                while hand1.hc == hand2.hc:
                    hand1.calculate_hc(nignore=i)
                    hand2.calculate_hc(nignore=i)
                    if hand1.hc > hand2.hc:
                        nwins += 1
                        # print('Player 1 wins')
                        break
                    i += 1
            # else:
            #     print('Player 2 wins')

        # else:
        #     print('Player 2 wins')
    # else:
    #     print('Player 2 wins')
    j += 1
print(nwins)

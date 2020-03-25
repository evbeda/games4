from love_letter.card import Card
from love_letter.cards.baron import Baron
from love_letter.cards.countess import Countess
from love_letter.cards.guard import Guard
from love_letter.cards.handmaid import Handmaid
from love_letter.cards.king import King
from love_letter.cards.priest import Priest
from love_letter.cards.prince import Prince
from love_letter.cards.princess import Princess
import random


class Deck:

    def __init__(self):
        self.cards = []
        guards = [Guard() for index in range(5)]
        barons = [Baron() for index in range(2)]
        countesses = [Countess() for index in range(1)]
        handmaids = [Handmaid() for index in range(2)]
        king = [King() for index in range(1)]
        princes = [Prince() for index in range(2)]
        princess = [Princess() for index in range(1)]
        priests = [Priest() for index in range(2)]
        self.cards.extend(guards)
        self.cards.extend(barons)
        self.cards.extend(countesses)
        self.cards.extend(handmaids)
        self.cards.extend(king)
        self.cards.extend(princes)
        self.cards.extend(princess)
        self.cards.extend(priests)
        self.players = []

    def shuffle_cards(self):
       random.shuffle(self.cards)
       return self.cards

    def remove_last(self):
        self.cards.pop(-1)
        return self.cards

    def get_one_card(self):
        return self.cards.pop(0)

    def show_three(self):
        card_showed = []
        for index in range(3):
            card_showed.append(self.cards.pop(index))
        return card_showed

    def __str__(self):
        return "Deck : {} remaining cards".format(len(self.cards))

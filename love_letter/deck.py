from love_letter.card import Card
from love_letter.cards.baron import Baron
from love_letter.cards.countess import Countess
from love_letter.cards.guard import Guard
from love_letter.cards.handmaid import Handmaid
from love_letter.cards.king import King
from love_letter.cards.priest import Priest
from love_letter.cards.prince import Prince
from love_letter.cards.princess import Princess


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

from .cards.countess import Countess
from .cards.king import King
from .cards.prince import Prince


class Player(object):

    def __init__(self, game=None):
        self.name = None
        self.hearts = 0
        self.score = 0
        self.cards = []
        self.is_active = True
        self.discarded = []
        self.game = game

    def draw_card(self, card):
        card.player = self
        self.cards.append(card)

    def __str__(self):
        cards = ""
        for index in range(len(self.cards)):
            cards += "{}-{} ".format(index, self.cards[index].name)
        cards.strip(" ")
        return "Player: {}, " \
               "Hearts: {}, " \
               "Cards: {}".format(self.name, self.hearts, cards)

    def discard_card(self, card):
        self.cards.remove(card)
        self.score += card.score
        self.discarded.insert(0, card)
        card.player = None

    def reset_round(self):
        self.score = 0
        for card in self.cards:
            card.player = None
        self.cards = []
        self.discarded = []
        self.is_active = True

    def show_card(self):
        return self.cards[0]

    def ask_card(self):
        return self.game.get_deck_card()

    def get_heart(self):
        return self.hearts

    def select_card(self, string_index):
        index = int(string_index)
        selected_card = self.cards[index]
        if self.must_discard_countess():
            if not isinstance(selected_card, Countess):
                raise CountessNotDiscardedException

        return selected_card

    def must_discard_countess(self):
        has_king_or_prince = False
        has_countess = False
        for card in self.cards:
            if isinstance(card, (King, Prince)):
                has_king_or_prince = True
            elif isinstance(card, Countess):
                has_countess = True
        return has_countess and has_king_or_prince


class CountessNotDiscardedException(Exception):
    pass

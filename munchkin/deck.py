import random


class Deck:

    def __init__(self):
        self._cards = []
        self._discard_cards = []

    @property
    def cards(self):
        return self._cards

    @property
    def discard_cards(self):
        return self._discard_cards

    def add_discard(self, card_to_add):
        self._discard_cards.append(card_to_add)

    def add_cards(self, cards_to_add):
        self._cards.extend(cards_to_add)

    def shuffle_deck(self):
        random.shuffle(self._cards)

    def reset_cards(self):
        self._cards = self._discard_cards
        self.shuffle_deck()


class DoorDeck(Deck):

    def __init__(self):
        super().__init__()
        self.add_cards(["doorcard1", "doorcard2", "doorcard3", "doorcard4"])


class TreasureDeck(Deck):

    def __init__(self):
        super().__init__()
        self.add_cards(["treasurecard1", "treasurecard2", "treasurecard3", "treasurecard4"])

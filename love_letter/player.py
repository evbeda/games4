class Player:

    def __init__(self):
        self.name = None
        self.hearts = 0
        self.cards = []

    def set_a_card(self, card):
        self.cards.append(card)

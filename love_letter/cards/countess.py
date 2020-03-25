from love_letter.card import Card


class Countess(Card):
    def __init__(self):
        self.name = "Countess"
        self.score = 7
        self.description = "If a player holds both this card and either the King or Prince card, this card must be played immediately."

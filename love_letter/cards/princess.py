from love_letter.card import Card


class Princess(Card):

    def __init__(self):
        self.name = "Princess"
        self.score = 8
        self.description = "If a player plays this card for any reason, they are eliminated from the round."

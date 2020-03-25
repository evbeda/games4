from love_letter.card import Card


class King(Card):
    def __init__(self):
        self.name = "King"
        self.score = 6
        self.description = "Player trades hands with any other player."

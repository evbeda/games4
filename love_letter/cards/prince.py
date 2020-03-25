from love_letter.card import Card


class Prince(Card):
    def __init__(self):
        self.name = "Prince"
        self.score = 5
        self.description = "Player can choose any player (including themselves) to discard their hand and draw a new one. If the discarded card is the Princess, the discarding player is eliminated."

from love_letter.card import Card
from love_letter.player import Player


class Countess(Card):
    def __init__(self):
        super().__init__()
        self.name = "Countess"
        self.score = 7
        self.description = "If a player holds both this card and either the King or Prince card," \
                           " this card must be played immediately."

    def must_discard(self, player):
        for card in player.cards:
            if card.name == "King" or card.name == "Prince" :
                return True
        return False

    def execute_action(self, player):
        pass

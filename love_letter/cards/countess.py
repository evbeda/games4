from love_letter.card import Card
from love_letter.player import Player


class Countess(Card):

    input_instructions = "Countess input instructions:\n" \
                         "'card number'\n" \
                         "example: 2"

    def __init__(self):
        super().__init__()
        self.name = "Countess"
        self.score = 7
        self.description = "If a player holds both this card and either the King or Prince card," \
                           " this card must be played immediately."

    def must_discard(self):
        for card in self.player.cards:
            if card.name == "King" or card.name == "Prince":
                return True
        return False

    def execute_action(self):
        pass

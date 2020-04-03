from love_letter.card import Card


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

    def execute_action(self):
        pass

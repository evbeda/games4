from love_letter.card import Card


class Handmaid(Card):

    input_instructions = "Handmaid input instructions:\n" \
                         "'card number'\n" \
                         "example: 1"

    def __init__(self):
        super().__init__()
        self.name = "Handmaid"
        self.score = 4
        self.description = "Player cannot be affected by any other player's card until the next turn."
     
    def execute_action(self):
        pass

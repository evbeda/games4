from love_letter.card import Card


class King(Card):

    input_instructions = "King input instructions:\n" \
                         "'card number-opponent number'\n" \
                         "example: 2-1"

    def __init__(self):
        super().__init__()
        self.name = "King"
        self.score = 6
        self.description = "Player trades hands with any other player."

    def execute_action(self, target):
        player_card = self.player.cards[0]
        target_card = target.cards[0]
        self.player.cards[0] = target_card
        target.cards[0] = player_card


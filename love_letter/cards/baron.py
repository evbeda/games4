from love_letter.card import Card


class Baron(Card):

    input_instructions = "Baron input instructions:\n" \
                         "'card number-opponent number'\n" \
                         "example: 1-2"

    def __init__(self):
        super().__init__()
        self.name = "Baron"
        self.score = 3
        self.description = "Player will choose another player and privately compare hands." \
                           " The player with the lower-strength hand is eliminated from the round."

    def execute_action(self, target):
        player_card = self.player.show_card()
        target_card = target.show_card()

        if player_card.score > target_card.score:
            target.is_active = False
        elif target_card.score > player_card.score:
            self.player.is_active = False
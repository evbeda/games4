from love_letter.card import Card


class Prince(Card):

    input_instructions = "Prince input instructions:\n" \
                         "'card number-opponent number' or 'card-number'\n" \
                         "Example: 1-2 for opponent and 1 for choosing self"

    def __init__(self):
        super().__init__()
        self.name = "Prince"
        self.score = 5
        self.description = "Player can choose any player (including themselves)" \
                           " to discard their hand and draw a new one. " \
                           "If the discarded card is the Princess, the discarding player is eliminated."

    def execute_action(self, target=None):
        if target.cards[0].name == "Princess":
            target.is_active = False
        target.discarded.append(target.cards.pop())
        card_to_draw = self.player.ask_card()
        target.draw_card(card_to_draw)


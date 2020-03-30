from love_letter.card import Card


class Guard(Card):

    input_instructions = "Guard input instructions:\n" \
                         "'card number-opponent number-guess of the card'\n" \
                         "example: 1-2-king"

    def __init__(self):
        super().__init__()
        self.name = "Guard"
        self.score = 1
        self.description = "Player designates another player and names a type of card." \
                           " If that player's hand matches the type of card specified," \
                           " that player is eliminated from the round. However," \
                           " Guard cannot be named as the type of card."
    
    def execute_action(self, target, card):
        target_card = target.show_card()
        if card == target_card.name and target_card.name != "Guard":
            target.is_active = False
            return True
        else:
            return False



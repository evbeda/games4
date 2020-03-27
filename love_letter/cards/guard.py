from love_letter.card import Card


class Guard(Card):
    def __init__(self):
        super().__init__()
        self.name = "Guard"
        self.score = 1
        self.description = "Player designates another player and names a type of card." \
                           " If that player's hand matches the type of card specified," \
                           " that player is eliminated from the round. However," \
                           " Guard cannot be named as the type of card."




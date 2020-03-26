from love_letter.card import Card


class Baron(Card):
    def __init__(self):
        self.name = "Baron"
        self.score = 3
        self.description = "Player will choose another player and privately compare hands." \
                           " The player with the lower-strength hand is eliminated from the round."

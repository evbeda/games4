from love_letter.card import Card


class King(Card):
    def __init__(self):
        self.name = "King"
        self.score = 6
        self.description = "Player trades hands with any other player."

    def execute_action(self, player, target):
        player_card = player.cards[0]
        target_card = target.cards[0]
        player.cards[0] = target_card
        target.cards[0] = player_card


from love_letter.card import Card


class Priest(Card):

    def __init__(self):
        super().__init__()
        self.name = "Priest"
        self.score = 2
        self.description = "Player is allowed to see another player's hand."

    def execute_action(self, player, target=None):
        card_to_show = target.show_card()
        return card_to_show.__str__()

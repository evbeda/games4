from love_letter.player import Player


class HumanPlayer(Player):

    def __init__(self, name, deck=None):
        super().__init__(deck)
        self.name = name

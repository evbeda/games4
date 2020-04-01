from love_letter.player import Player


class HumanPlayer(Player):

    def __init__(self, name, game=None):
        super().__init__(game)
        self.name = name
from love_letter.player import Player


class PcPlayer(Player):

    def __init__(self, game=None):
        super().__init__(game)
        self.name = "PC Player"

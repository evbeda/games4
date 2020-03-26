from love_letter.player import Player


class PcPlayer(Player):

    def __init__(self, deck=None):
        super().__init__(deck)
        self.name = "PC Player"

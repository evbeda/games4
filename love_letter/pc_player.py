from love_letter.player import Player


class PcPlayer(Player):

    def __init__(self, deck = None):
        super(PcPlayer, self).__init__()
        self.name = "PC Player"

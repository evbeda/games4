from love_letter.player import Player


class PcPlayer(Player):

    def __init__(self):
        super(PcPlayer, self).__init__()
        self.name = "PC Player"

from love_letter.player import Player


class HumanPlayer(Player):

    def __init__(self,name):
        super(HumanPlayer, self).__init__()
        self.name = name
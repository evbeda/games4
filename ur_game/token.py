class Token:

    def __init__(self, index=None, player=None):
        self.player = player
        if index is None:
            self.index = 0
        else:
            self.index = index

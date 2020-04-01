class Token:

    def __init__(self, index=None):
        self.player = None
        if index is None:
            self.index = 0
        else:
            self.index = index

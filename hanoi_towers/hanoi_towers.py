from .tower import Tower


class HanoiTowers:

    def __init__(self, cant_tokens):
        self.cant_tokens = cant_tokens
        self.tower1 = Tower(cant_tokens)
        self.tower2 = Tower()
        self.tower3 = Tower()

    def next_turn(self):

        if (len(self.tower3.tokens) == self.cant_tokens) or (len(self.tower2.tokens) == self.cant_tokens):
            return "You won"
        else:
            return "Plase make your move"

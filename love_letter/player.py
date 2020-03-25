class Player(object):

    def __init__(self):
        self.name = None
        self.hearts = 0
        self.score = 0
        self.cards = []
        self.is_active = True

    def set_a_card(self, card):
        self.cards.append(card)


    def __str__(self):
        return "Player: {}, " \
               "Hearts: {}".format(self.name, self.hearts)


    def discard_card(self, card):
        self.cards.remove(card)
        self.score += card.score
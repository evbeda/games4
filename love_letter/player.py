class Player(object):

    def __init__(self, deck = None):
        self.name = None
        self.hearts = 0
        self.score = 0
        self.cards = []
        self.is_active = True
        self.discarded = []
        self.deck = deck

    def draw_card(self):
        self.cards.append(self.deck.pop())

    def __str__(self):
        return "Player: {}, " \
               "Hearts: {}".format(self.name, self.hearts)

    def discard_card(self, card):
        self.cards.remove(card)
        self.score += card.score
        self.discarded.insert(0, card)

    def end_of_round(self):
        self.score = 0
        self.cards = []
        self.discarded = []

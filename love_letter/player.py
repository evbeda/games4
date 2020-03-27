class Player(object):

    def __init__(self, game=None):
        self.name = None
        self.hearts = 0
        self.score = 0
        self.cards = []
        self.is_active = True
        self.discarded = []
        self.game = game

    def draw_card(self, card):
        card.player = self
        self.cards.append(card)

    def __str__(self):
        return "Player: {}, " \
               "Hearts: {}".format(self.name, self.hearts)

    def discard_card(self, card):
        self.cards.remove(card)
        self.score += card.score
        self.discarded.insert(0, card)
        card.player = None

    def end_of_round(self):
        self.score = 0
        for card in self.cards:
            card.player = None
        self.cards = []
        self.discarded = []
        self.is_active = True

    def show_card(self):
        return self.cards[0]

    def ask_card(self):
        return self.game.get_deck_card()
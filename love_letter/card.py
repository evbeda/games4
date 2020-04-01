class Card:

    def __init__(self):
        self.score = None
        self.name = None
        self.description = None
        self.player = None

    def execute_action(self, target=None):
        raise Exception("Not implemented action!")

    def __str__(self):
        return "Name: {}, " \
               "Strength: {}, " \
               "Description: {}".format(self.name,self.score,self.description)

class Card:

    def __init__(self, cardDictionary):
        self.name = cardDictionary["name"]
        self.type = cardDictionary["type"]
        self.subtype = cardDictionary["subtype"]
        self.effects = cardDictionary["effects"]
        self.description = cardDictionary["description"]
        self.player = None

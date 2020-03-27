class Card:

    def __init__(self):
        self.score = None
        self.name = None
        self.description = None
        self.player = None

    def execute_action(self, target=None):
        raise Exception("Not implemented action!")

    def must_discard(self, player):
        return False

    def look_for_handmaid(self, players, player_owner):
        save_players = []
        for player in players:
            if player == player_owner:
                pass
            if len(player.discarded) > 0 and player.discarded[0].name == "Handmaid":
                save_players.append(player)
        return save_players

    def __str__(self):
        return "Name: {}, " \
               "Strength: {}, " \
               "Description: {}".format(self.name,self.score,self.description)

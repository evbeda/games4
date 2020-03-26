from love_letter.card import Card


class King(Card):
    def __init__(self):
        self.name = "King"
        self.score = 6
        self.description = "Player trades hands with any other player."

    def look_for_handmaid(self, players, player_owner):
        save_players = []
        for player in players:
            if player == player_owner:
                pass
            if len(player.discarded) > 0 and player.discarded[0].name == "Handmaid":
                save_players.append(player)
        return save_players

    def execute_action(self, player):
        pass


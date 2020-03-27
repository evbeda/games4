from love_letter.card import Card


class Baron(Card):
    def __init__(self):
        self.name = "Baron"
        self.score = 3
        self.description = "Player will choose another player and privately compare hands." \
                           " The player with the lower-strength hand is eliminated from the round."

    def execute_action(self, player, target):
        player_card = player.show_card(target)
        target_card = target.show_card(player)

        if player_card.score > target_card.score:
            target.is_active = False
        elif target_card.score > player_card.score:
            player.is_active = False
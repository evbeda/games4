from ur_game.token import Token


class Player:
    def __init__(self):
        self.initial = [Token() for _ in range(7)]

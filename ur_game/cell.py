class Cell:

    def __init__(self, is_special=False):
        self.token = None
        self.__is_special = is_special

    @property
    def is_empty(self):
        return self.token is None

    def put_token(self, token):
        self.token = token

    def clear_cell(self):
        token = self.token
        self.token = None
        return token

    def set_special(self):
        self.__is_special = True

    @property
    def is_special(self):
        return self.__is_special

    def __str__(self):
        if self.is_empty:
            ""
        else:
            return self.token.player.token_type

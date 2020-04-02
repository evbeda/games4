class Cell:

    def __init__(self, is_special=False):
        self.token = None
        self.is_special = is_special

    @property
    def is_empty(self):
        return self.token is None

    def put_token(self, token):
        self.token = token

    def clear_cell(self):
        self.token = None

    def set_special(self):
        self.is_special = True

    @property
    def is_special(self):
        return self.is_special

class Cell:

    def __init__(self):
        self.token = None

    @property
    def is_empty(self):
        return self.token is None

    def put_token(self, token):
        self.token = token

    def clear_cell(self):
        self.token = None

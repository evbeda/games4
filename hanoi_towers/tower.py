from .token import Token


class Tower:
    
    def __init__(self, cant_tokens=0):
        self.tokens = []
        for i in range(cant_tokens):
            self.tokens.insert(0, Token(i+1))

    def insert_token(self, token):
        if(self.validate_insert_token(token)):
            self.tokens.append(token)
    
    def validate_insert_token(self, token):
        if len(self.tokens) == 0:
            return True
        elif self.tokens[-1].size > token.size:
            return True
        return False

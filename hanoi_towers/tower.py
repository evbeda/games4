from .token import Token


class Tower:
    
    def __init__(self, cant_tokens=0):
        self.tokens = []
        for i in range(cant_tokens):
            self.tokens.insert(0, Token(i+1))

    # def push_token(self, token):
    #     if(self.validate_push_token(self.token)):
    #         self.t

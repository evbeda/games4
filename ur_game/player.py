from ur_game.cell import Cell
from ur_game.token import Token


class Player:
    def __init__(self, shared=[], id_number=0):
        self.shared = shared
        self.initial = [Token(i, self) for i in range(7)]
        self.final_stack = []
        self.start = [Cell() for _ in range(4)]
        self.start[3].set_special()
        self.finish = [Cell() for _ in range(2)]
        self.finish[0].set_special()
        self.addition_turn = False
        self.id_number = id_number + 1
        self.type = None
        if self.id_number == 1:
            self.token_type = "O"
        else:
            self.token_type = "X"

    def validate_movement_from_cell(self, from_index):
        from_cell = self.get_cell_by_index(from_index)

        if from_cell.token is None or from_cell.token.player is not self:
            raise InvalidMovementException("You don't have any token in this cell")
        return from_cell

    def validate_movement_to_cell(self, to_index):
        to_cell = self.get_cell_by_index(to_index)

        if to_cell.token is not None and to_cell.token.player is self:
            raise InvalidMovementException("You cannot move to this cell because you have a token there")
        
        elif to_cell.token is not None and to_cell.is_special and to_cell.token is not self:
            raise TokenProtectedException("You cannot move to this cell because the opponent is protected in there")
        
        elif to_cell.is_special:
            self.addition_turn = True
        return to_cell


    def validate_movement_from_initial(self):
        if len(self.initial) == 0:
            raise InvalidMovementException("You dont have more Tokens")

    def move_token_from_initial_to_cell(self, to_cell):
        token = self.initial.pop()
        self.move_token_to_cell(to_cell, token)

    def move_token_from_cell_to_cell(self, from_cell, to_cell):
        token = from_cell.clear_cell()  # limpiar la celda anterior
        # verificar si hay otra ficha -> comer
        if to_cell.token is not None:
            # sacar la ficha del oponente
            enemy_token = to_cell.clear_cell()
            # devolversela al oponente -> initial.append
            enemy_token.player.initial.append(enemy_token)
        self.move_token_to_cell(to_cell, token)  # moviendo

    def move_token_to_cell(self, to_cell, token):
        if to_cell == self.finish[-1]:
            self.final_stack.append(token)
        else:
            to_cell.put_token(token)

    def get_cell_by_index(self, index):
        if index < 1 or index > len(self.start + self.shared + self.finish):
            raise OutOfBoardException
        return (self.start + self.shared + self.finish)[index - 1]

    def move_token(self, dice_result, index_token):
        to_cell = self.validate_movement_to_cell(index_token + dice_result)

        if index_token == 0:
            self.validate_movement_from_initial()
            self.move_token_from_initial_to_cell(to_cell)
        else:
            from_cell = self.validate_movement_from_cell(index_token)
            self.move_token_from_cell_to_cell(from_cell, to_cell)

    def initial_and_final_arr_str(self):
        initial_arr = "["
        ini = 4
        for cell in reversed(self.start):
            if not cell.is_empty and ini > 1:
                initial_arr += " {},".format(cell.__str__())
            elif not cell.is_empty and ini == 1:
                initial_arr += " {}".format(cell.__str__())
            elif cell.is_special and ini > 1:
                initial_arr += "*{},".format(ini)
            elif not cell.is_special and ini > 1:
                initial_arr += " {},".format(ini)
            else:
                initial_arr += " {}".format(ini)
            ini -= 1
        initial_arr += "]"

        final_arr = "["
        ini = 14
        for cell in reversed(self.finish):
            if cell.is_empty and ini == 14:
                final_arr += "*{},".format(ini)
            elif cell.is_empty and ini == 13:
                final_arr += " {}".format(ini)
            else:
                initial_arr += " {},".format(cell.__str__())
            ini -= 1
        final_arr += "]"

        return initial_arr + " " * 7 + final_arr

    def __str__(self):
        return "Player{} number of initial  tokens: {}\n" \
               "Player{} number of finished tokens: {}\n" \
               "Player{} type of token: {}".format(
                self.id_number,
                len(self.initial),
                self.id_number,
                len(self.final_stack),
                self.id_number,
                self.token_type
        )


class InvalidMovementException(Exception):
    pass


class OutOfBoardException(Exception):
    pass


class TokenProtectedException(Exception):
    pass

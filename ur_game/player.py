from ur_game.cell import Cell
from ur_game.token import Token


class Player:
    def __init__(self, shared=None):
        self.shared = shared
        self.initial = [Token(i, self) for i in range(7)]
        self.final_stack = []
        self.start = [Cell(False) for _ in range(4)]
        self.start[3].set_special()
        self.finish = [Cell(False) for _ in range(2)]
        self.finish[0].set_special()

    def validate_movement_from_cell(self, from_index):
        from_cell = self.get_cell_by_index(from_index)

        if from_cell.token is None or from_cell.token.player is not self:
            raise InvalidMovementException("You don't have any token in this cell")
        return from_cell

    def validate_movement_to_cell(self, to_index):
        to_cell = self.get_cell_by_index(to_index)

        if to_cell.is_special and to_cell in self.shared:
            to_cell = self.get_cell_by_index(to_index + 1)

        if to_cell.token is not None and to_cell.token.player is self:
            raise InvalidMovementException("You cannot move to this cell because you have a token there")
        return to_cell

    def validate_movement_from_initial(self):
        if len(self.initial) == 0:
            raise InvalidMovementException("You dont have more Tokens")

    def move_token_from_initial_to_cell(self, to_cell):
        token = self.initial.pop()
        self.move_token_to_cell(to_cell, token)

    def move_token_from_cell_to_cell(self, from_cell, to_cell):
        token = from_cell.clear_cell()
        self.move_token_to_cell(to_cell, token)

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


class OccupedCellException(Exception):
    pass


class InvalidMovementException(Exception):
    pass


class OutOfBoardException(Exception):
    pass

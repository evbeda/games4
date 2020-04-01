from ur_game.cell import Cell
from ur_game.token import Token


class Player:
    def __init__(self, shared=None):
        self.shared = shared
        self.initial = [Token(i, self) for i in range(7)]
        self.final_stack = []
        self.start = [Cell() for _ in range(4)]
        self.finish = [Cell() for _ in range(2)]

    def move_token(self, dice_result, index_token):

        if dice_result == 0:
            return None

        my_index, actual_array = self.search_token(index_token)

        if actual_array == self.initial:
            my_token = actual_array.pop(my_index)
        else:
            my_token = actual_array[my_index].token
            actual_array[my_index].clear_cell()

        if actual_array == self.initial:
            if not self.start[dice_result - 1].is_empty:
                raise OccupedCellException
            else:
                self.start[dice_result - 1].put_token(my_token)
        elif actual_array == self.start:
            if dice_result + my_index > 3:
                if not self.shared[abs(my_index - 4 + dice_result)].is_empty:
                    raise OccupedCellException
                else:
                    self.shared[abs(my_index - 4 + dice_result)].put_token(my_token)
            else:
                if not self.start[my_index + dice_result].is_empty:
                    raise OccupedCellException
                else:
                    self.start[my_index + dice_result].put_token(my_token)
        elif actual_array == self.shared:
            if dice_result + my_index > 7:
                if abs(my_index - 8 + dice_result) == 1:
                    self.final_stack.append(my_token)
                else:
                    if not self.finish[abs(my_index - 8 + dice_result)].is_empty:
                        raise OccupedCellException
                    else:
                        self.finish[abs(my_index - 8 + dice_result)].put_token(my_token)
            else:
                if not self.shared[my_index + dice_result].is_empty:
                    raise OccupedCellException
                else:
                    self.shared[my_index + dice_result].put_token(my_token)
        elif actual_array == self.finish:
            if dice_result == 1:
                self.final_stack.append(my_token)
            else:
                return None

    def search_token(self, token_index):
        search_result_in_array_with_tokens = self.__search_array_with_tokens(token_index)
        search_result_in_array_with_cells = self.__search_array_with_cells(token_index)
        if search_result_in_array_with_tokens:
            return search_result_in_array_with_tokens
        return search_result_in_array_with_cells

    def __search_array_with_tokens(self, token_index):
        arrays_with_tokens = [self.initial, self.final_stack]
        for array in arrays_with_tokens:
            for token_index_array in range(len(array)):
                if array[token_index_array].index is token_index:
                    return token_index_array, array,
        return None

    def __search_array_with_cells(self, token_index):
        arrays_with_cells = [self.start, self.shared, self.finish]
        for array in arrays_with_cells:
            for cell_index in range(len(array)):
                if not array[cell_index].is_empty and array[cell_index].token.index is token_index:
                    return cell_index, array,
        return None


class OccupedCellException(Exception):
    pass

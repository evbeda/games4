from ur_game.cell import Cell
from ur_game.token import Token


class Player:
    def __init__(self, shared=None):
        self.shared = shared
        self.initial = [Token(i) for i in range(7)]
        self.final_stack = []
        self.start = [Cell() for _ in range(4)]
        self.finish = [Cell() for _ in range(2)]

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



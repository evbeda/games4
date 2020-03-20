import unittest
from senku.senku import Senku, SenkuInvalidMovementException, SenkuMovementOutOfRangeException


class TestSenku(unittest.TestCase):

    def setUp(self):
        self.game = Senku()

    def test_get_board_initial(self):
        self.assertEqual(
            self.game.board,
            "X X 0 0 0 X X\n"
            "X X 0 0 0 X X\n"
            "0 0 0 0 0 0 0\n"
            "0 0 0 - 0 0 0\n"
            "0 0 0 0 0 0 0\n"
            "X X 0 0 0 X X\n"
            "X X 0 0 0 X X"
        )

    def test_validate_move_up(self):
        self.assertTrue(SenkuMovementOutOfRangeException, self.game.validate_move(5, 3, 3, 3))

    def test_validate_move_down(self):
        self.assertTrue(SenkuMovementOutOfRangeException, self.game.validate_move(1, 3, 3, 3))

    def test_validate_move_right(self):
        self.assertTrue(SenkuMovementOutOfRangeException, self.game.validate_move(3, 1, 3, 3))

    def test_validate_move_left(self):
        self.assertTrue(SenkuMovementOutOfRangeException, self.game.validate_move(3, 5, 3, 3))

    def test_validate_move_out_of_range_up(self):
        self.assertRaises(SenkuMovementOutOfRangeException, self.game.validate_move, 0, 0, -1, 0)

    def test_validate_move_out_of_range_down(self):
        self.assertRaises(SenkuMovementOutOfRangeException, self.game.validate_move, 6, 6, 7, 6)

    def test_validate_move_out_of_range_right(self):
        self.assertRaises(SenkuMovementOutOfRangeException, self.game.validate_move, 6, 6, 6, 7)

    def test_validate_move_out_of_range_left(self):
        self.assertRaises(SenkuMovementOutOfRangeException, self.game.validate_move, 0, 0, 0, -1)

    def test_validate_diagonal_move(self):
        self.assertRaises(SenkuMovementOutOfRangeException, self.game.validate_move, 3, 2, 4, 3)

    def test_validate_move_right_with_free_space_between(self):
        self.game.set_board([['0', '-', '-'], ['0', '0', '0']])
        self.assertRaises(SenkuInvalidMovementException, self.game.validate_move, 0, 0, 0, 2)

    def test_validate_move_left_with_free_space_between(self):
        self.game.set_board([['-', '-', '0'], ['0', '0', '0']])
        self.assertRaises(SenkuInvalidMovementException, self.game.validate_move, 0, 2, 0, 0)

    def test_validate_move_up_with_free_space_between(self):
        self.game.set_board([['-', '0', '0'], ['-', '0', '0'], ['0', '0', '0']])
        self.assertRaises(SenkuInvalidMovementException, self.game.validate_move, 2, 0, 0, 0)

    def test_validate_move_down_with_free_space_between(self):
        self.game.set_board([['0', '0', '0'], ['-', '0', '0'], ['-', '0', '0']])
        self.assertRaises(SenkuInvalidMovementException, self.game.validate_move, 0, 0, 2, 0)

    def test_move_piece_col(self):
        self.game.play(3, 1, 3, 3)
        self.assertEqual(
            self.game.board,
            "X X 0 0 0 X X\n"
            "X X 0 0 0 X X\n"
            "0 0 0 0 0 0 0\n"
            "0 - - 0 0 0 0\n"
            "0 0 0 0 0 0 0\n"
            "X X 0 0 0 X X\n"
            "X X 0 0 0 X X"
        )

    def test_move_piece_row(self):
        self.game.play(1, 3, 3, 3)
        self.assertEqual(
            self.game.board,
            "X X 0 0 0 X X\n"
            "X X 0 - 0 X X\n"
            "0 0 0 - 0 0 0\n"
            "0 0 0 0 0 0 0\n"
            "0 0 0 0 0 0 0\n"
            "X X 0 0 0 X X\n"
            "X X 0 0 0 X X"
        )

    def test_get_board(self):
        test_array = [1, 2, 3, 4]
        self.game.set_board(test_array)
        self.assertEqual(self.game._board, self.game.get_board())

    def test_set_board(self):
        test_array = [1, 2, 3, 4]
        self.game.set_board(test_array)
        self.assertEqual(test_array, self.game.get_board())


if __name__ == "__main__":
    unittest.main()

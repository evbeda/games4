import unittest

from senku import SenkuGame, SenkuMovementOutOfRangeException, SenkuInvalidMovementException


class TestSenku(unittest.TestCase):

    def setUp(self):
        self.game = SenkuGame()

    def test_get_board_initial(self):
        self.assertEqual(
            self.game.get_board(),
            [
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '-', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
            ]
        )

    def test_validate_print_board(self):
        self.assertEqual(
            self.game.board,
            "  0 1 2 3 4 5 6\n"
            " + = = = = = = =\n"
            "0| X X 0 0 0 X X\n"
            "1| X X 0 0 0 X X\n"
            "2| 0 0 0 0 0 0 0\n"
            "3| 0 0 0 - 0 0 0\n"
            "4| 0 0 0 0 0 0 0\n"
            "5| X X 0 0 0 X X\n"
            "6| X X 0 0 0 X X\n"
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
        self.assertRaises(SenkuInvalidMovementException, self.game.validate_move, 2, 2, 3, 3)

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
            self.game.get_board(),
            [
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '-', '-', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
            ]
        )

    def test_move_piece_row(self):
        self.game.play(1, 3, 3, 3)
        self.assertEqual(
            self.game.get_board(),
            [
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['X', 'X', '0', '-', '0', 'X', 'X'],
                ['0', '0', '0', '-', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
                ['X', 'X', '0', '0', '0', 'X', 'X'],
            ]
        )

    def test_get_board(self):
        test_array = [1, 2, 3, 4]
        self.game.set_board(test_array)
        self.assertEqual(self.game._board, self.game.get_board())

    def test_set_board(self):
        test_array = [1, 2, 3, 4]
        self.game.set_board(test_array)
        self.assertEqual(test_array, self.game.get_board())

<<<<<<< Updated upstream
    def check_lose_game(self):
        self.game.set_board([
            ['X', 'X', '0', '-', '0', 'X', 'X'],
            ['X', 'X', '-', '-', '-', 'X', 'X'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '0', '-', '0', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['X', 'X', '-', '-', '-', 'X', 'X'],
            ['X', 'X', '-', '-', '-', 'X', 'X'],
        ])
        self.assertEqual(self.game.check_loose(), True)
=======
    def test_next_turn_win(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You won")
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_0(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '0', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.check_loose(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_1(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '0', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_2(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '0', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_3(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '0', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_4(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '0', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_5(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '0', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_6(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '0', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_7(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '0', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_lose_8(self):
        self.game.set_board([
                            ['X', 'X', '0', '0', '0', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "You loose")
        self.assertTrue(self.game.check_loose())
        self.assertFalse(self.game.is_playing)

    def test_next_turn_playing_0(self):
        self.game.set_board([
                            ['X', 'X', '0', '0', '0', 'X', 'X'],
                            ['X', 'X', '0', '0', '0', 'X', 'X'],
                            ['0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '-', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0'],
                            ['X', 'X', '0', '0', '0', 'X', 'X'],
                            ['X', 'X', '0', '0', '0', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "Please, make a move")
        self.assertTrue(self.game.is_playing)

    def test_next_turn_playing_1(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '0', '0', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "Please, make a move")
        self.assertTrue(self.game.is_playing)

    def test_next_turn_playing_2(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '0', '-', 'X', 'X'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "Please, make a move")
        self.assertTrue(self.game.is_playing)

    def test_next_turn_playing_3(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '0', '0', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "Please, make a move")
        self.assertTrue(self.game.is_playing)

    def test_next_turn_playing_4(self):
        self.game.set_board([
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '0', '-', '-', '-'],
                            ['X', 'X', '-', '0', '-', 'X', 'X'],
                            ['X', 'X', '-', '-', '-', 'X', 'X'],
                            ])
        self.assertEqual(self.game.next_turn(), "Please, make a move")
        self.assertTrue(self.game.is_playing)

>>>>>>> Stashed changes

if __name__ == "__main__":
    unittest.main()

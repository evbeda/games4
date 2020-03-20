import unittest
from senku.senku import Senku


class TestSenku(unittest.TestCase):

    def setUp(self):
        self.game = Senku()

    def test_get_board_initial(self):
        self.assertEqual(self.game.board,
                         "X X 0 0 0 X X\n"
                         "X X 0 0 0 X X\n"
                         "0 0 0 0 0 0 0\n"
                         "0 0 0 - 0 0 0\n"
                         "0 0 0 0 0 0 0\n"
                         "X X 0 0 0 X X\n"
                         "X X 0 0 0 X X"
                         )

    def test_validate_move_up(self):
        self.assertTrue(self.game.validate_move(5, 3, 3, 3))

    def test_validate_move_down(self):
        self.assertTrue(self.game.validate_move(1, 3, 3, 3))

    def test_validate_move_right(self):
        self.assertTrue(self.game.validate_move(3, 1, 3, 3))

    def test_validate_move_left(self):
        self.assertTrue(self.game.validate_move(3, 5, 3, 3))

    def test_validate_move_out_of_range_up(self):
        self.assertFalse(self.game.validate_move(0, 0, -1, 0))

    def test_validate_move_out_of_range_down(self):
        self.assertFalse(self.game.validate_move(6, 6, 7, 6))

    def test_validate_move_out_of_range_right(self):
        self.assertFalse(self.game.validate_move(6, 6, 6, 7))

    def test_validate_move_out_of_range_left(self):
        self.assertFalse(self.game.validate_move(0, 0, 0, -1))


    def test_move_piece(self):
        self.game.play(3, 1, 3, 3)
        self.assertEqual(self.game.board,
                         "X X 0 0 0 X X\n"
                         "X X 0 0 0 X X\n"
                         "0 0 0 0 0 0 0\n"
                         "0 - - 0 0 0 0\n"
                         "0 0 0 0 0 0 0\n"
                         "X X 0 0 0 X X\n"
                         "X X 0 0 0 X X"
                         )


if __name__ == "__main__":
    unittest.main()

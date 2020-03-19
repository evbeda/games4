import unittest
from senku import Senku


class TestSenku(unittest.TestCase):

    def setUp(self):
        self.game = Senku()

    def test_get_board_initial(self):
        self.assertEqual(self.game.show_board(),
                         "X X 0 0 0 X X\n"
                         "X X 0 0 0 X X\n"
                         "0 0 0 0 0 0 0\n"
                         "0 0 0 - 0 0 0\n"
                         "0 0 0 0 0 0 0\n"
                         "X X 0 0 0 X X\n"
                         "X X 0 0 0 X X"
                         )

    def test_validate_move(self):
        self.assertTrue(self.game.validate_move(3, 1, 3, 3))
        self.assertFalse(self.game.validate_move(3, 2, 3, 3))
        self.assertFalse(self.game.validate_move(0, 0, 3, 3))

    def test_validate_move_out_of_range(self):
        self.assertFalse(self.game.validate_move(9, 2, 3, 3))
        self.assertFalse(self.game.validate_move(3, 2, -2, 3))

    def test_move_piece(self):
        pass


if __name__ == "__main__":
    unittest.main()

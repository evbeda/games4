import unittest
from senku import Senku


class TestSenku(unittest.TestCase):

    def setUp(self):
        self.game = Senku()

    def test_get_board_initial(self):
        self.assertEqual(self.game.show_board(),
                         "x x 0 0 0 x x\n"
                         "x x 0 0 0 x x\n"
                         "0 0 0 0 0 0 0\n"
                         "0 0 0 - 0 0 0\n"
                         "0 0 0 0 0 0 0\n"
                         "x x 0 0 0 x x\n"
                         "x x 0 0 0 x x"
                         )

    def test_validate_move(self):
        self.assertTrue(self.game.validate_move(3, 1, 3, 3))
        self.assertFalse(self.game.validate_move(3, 2, 3, 3))

    def test_validate_move_out_of_range(self):
        self.assertFalse(self.game.validate_move(9, 2, 3, 3))


if __name__ == "__main__":
    unittest.main()

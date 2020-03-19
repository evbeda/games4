import unittest
from senku import Senku


class TestSenku(unittest.TestCase):

    def setUp(self):
        self.game = Senku()

    def test_get_board_initial(self):
        self.assertEqual(self.game.show_board(),
                       'x x 0 0 0 x x\nx x 0 0 0 x x\n0 0 0 0 0 0 0\n0 0 0 - 0 0 0\n0 0 0 0 0 0 0\nx x 0 0 0 x x\nx x 0 0 0 x x')


if __name__ == "__main__":
    unittest.main()
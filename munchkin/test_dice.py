import unittest
from .dice import Dice


class TestDice(unittest.TestCase):

    def test_dado_between_1_and_6(self):
        dice = Dice()
        result = dice.shuffle()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)


if __name__ == "__main__":
    unittest.main()

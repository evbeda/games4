import unittest
from dado import Dado
from monstruo import Monstruo

class TestMunchkin(unittest.TestCase) :
    def test_dado_between_1_and_6(self):
        dado = Dado()
        result = dado.shuffle()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_monstruo_has_level_greater_or_equal_than_1(self):
        monstruo = Monstruo()
        result = monstruo.get_level
        self.assertGreaterEqual(result, 1)
    
    def test_monstruo_has_treasures_greater_or_equal_than_1(self):
        monstruo = Monstruo()
        result = monstruo.get_treasures
        self.assertGreaterEqual(result, 1)        

    def test_monstruo_has_level_add_greater_or_equal_than_1(self):
        monstruo = Monstruo()
        result = monstruo.get_level
        self.assertGreaterEqual(result, 1)


if __name__ == "__main__" :
    unittest.main()
import unittest
from monster import Monster

class TestMonster(unittest.TestCase) :

    def test_monster_has_power_greater_or_equal_than_1(self):
        monster = Monster("CHUPACABRAS", 8, 1, 2)
        result = monster.power
        self.assertGreaterEqual(result, 1)
    
    def test_monster_has_treasures_greater_or_equal_than_1(self):
        monster = Monster("CHUPACABRAS", 8, 1, 2)
        result = monster.treasures
        self.assertGreaterEqual(result, 1)        

    def test_monster_has_level_add_greater_or_equal_than_1(self):
        monster = Monster("CHUPACABRAS", 8, 1, 2)
        result = monster.level_add
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 9)


if __name__ == "__main__" :
    unittest.main()
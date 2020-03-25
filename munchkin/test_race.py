import unittest
from .race import Race

class TestRace(unittest.TestCase):
    def test_race_has_5_cards_on_init(self):
        race = Race()
        result = race.max_cards
        self.assertGreaterEqual(result, 5)
	
    def test_race_cant_carry_objects_on_init(self):
        race = Race()
        result = race.carry_objects
        self.assertFalse(result)

if __name__ == "__main__" :
    unittest.main()
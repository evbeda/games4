import unittest
from race import Race

class TestRace(unittest.TestCase) :

    def test_race_dwarf_has_max_card_equals_6(self):
        race = Race("dwarf",6,1)
        result = race.max_cards
        self.assertEqual(result, 6)    
    
    def test_race_has_max_object_greater_or_equals_than_1(self):
        race = Race("dwarf",6,1)
        result = race.max_objects
        self.assertGreaterEqual(result, 1)
    

if __name__ == "__main__":
    unittest.main()
    
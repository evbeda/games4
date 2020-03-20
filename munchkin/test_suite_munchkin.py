import unittest
from test_dice import TestDice
from test_monster import TestMonster
from test_race import TestRace

# from dice import Dice
# from monster import Monster

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestDice))
    test_suite.addTest(unittest.makeSuite(TestMonster))
    test_suite.addTest(unittest.makeSuite(TestRace))
    return test_suite


if __name__ == "__main__" :
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
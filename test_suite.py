import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from senku.test_senku import TestSenku
from love_letter.test_love_letter import TestDeck

def suite():
    test_suite = unittest.TestSuite()
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestSenku))
    test_suite.addTest(unittest.makeSuite(TestDeck))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)

import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from love_letter.test_love_letter import TestLoveLetter
from senku.test_senku import TestSenku

def suite():
    test_suite = unittest.TestSuite()
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestLoveLetter))
    test_suite.addTest(unittest.makeSuite(TestSenku))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)

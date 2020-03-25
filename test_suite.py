import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from senku_game.test_senku import TestSenku
from love_letter.test_love_letter import TestDeck, TestPlayer, TestLoveLetterGame, TestCard
from ahorcado.test_ahorcado import TestAhorcado


def suite():
    test_suite = unittest.TestSuite()
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestSenku))
    # Love Letter Game
    test_suite.addTest(unittest.makeSuite(TestDeck))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestLoveLetterGame))
    test_suite.addTest(unittest.makeSuite(TestCard))
    # Ahorcado game
    test_suite.addTest(unittest.makeSuite(TestAhorcado))

    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)

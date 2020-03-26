import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from senku_game.test_senku import TestSenku
from love_letter.test_love_letter import TestDeck, TestPlayer, TestLoveLetterGame, TestCard, TestPrincess, TestCountess, TestKing
from ahorcado.test_ahorcado import TestAhorcado
from munchkin.test_dice import TestDice
from munchkin.test_monster import TestMonster
from munchkin.test_race import TestRace
from munchkin.test_player import TestMunchkinPlayer
from test_game import TestGame


def suite():
    test_suite = unittest.TestSuite()
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestSenku))
    #Munchkin
    test_suite.addTest(unittest.makeSuite(TestDice))
    test_suite.addTest(unittest.makeSuite(TestMonster))
    test_suite.addTest(unittest.makeSuite(TestRace))
    test_suite.addTest(unittest.makeSuite(TestMunchkinPlayer))
    #Love Letter Game
    test_suite.addTest(unittest.makeSuite(TestDeck))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestLoveLetterGame))
    test_suite.addTest(unittest.makeSuite(TestCard))
    test_suite.addTest(unittest.makeSuite(TestPrincess))
    test_suite.addTest(unittest.makeSuite(TestCountess))
    test_suite.addTest(unittest.makeSuite(TestKing))
    # Ahorcado game
    test_suite.addTest(unittest.makeSuite(TestAhorcado))
    # GAME MACHINE
    test_suite.addTest(unittest.makeSuite(TestGame))

    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)

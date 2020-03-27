import unittest
from .dice import Dice
from .player import Player
from .doors.monster import Monster
from .doors.races.race import Race
from .munchkin import Munchkin
from .deck import TreasureDeck
from .deck import DoorDeck


class TestDice(unittest.TestCase):

    def test_dado_between_1_and_6(self):
        dice = Dice()
        result = dice.shuffle()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)


class TestMonster(unittest.TestCase):

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


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("person")

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "person")
        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.on_hand, [])
        self.assertEqual(self.player.on_board, [])
        self.assertEqual(self.player.max_race_cards, 1)
        self.assertEqual(self.player.max_class_cards, 1)
        self.assertEqual(self.player.max_cards_on_hand, 5)
        self.assertEqual(self.player.fleeing_chance, -4)
        self.assertEqual(self.player.isTurn, False)

    def test_set_default_status(self):
        self.player.name = "changed"
        self.player.level = 4
        self.player.on_hand = ["card"]
        self.player.on_board = ["card"]
        self.player.max_class_cards = 2
        self.player.fleeing_chance = -2
        self.player.max_race_cards = 2
        self.player.max_cards_on_hand = 7
        self.player.isTurn = True
        self.player.set_default_status()
        self.assertEqual(self.player.name, "changed")
        self.assertEqual(self.player.level, 4)
        self.assertEqual(self.player.on_hand, ["card"])
        self.assertEqual(self.player.on_board, ["card"])
        self.assertEqual(self.player.max_race_cards, 1)
        self.assertEqual(self.player.max_class_cards, 1)
        self.assertEqual(self.player.max_cards_on_hand, 5)
        self.assertEqual(self.player.fleeing_chance, -4)
        self.assertEqual(self.player.isTurn, True)

    def test_level_up(self):
        self.player.level_up()
        self.assertEqual(self.player.level, 2)

    def test_level_down(self):
        self.player.level = 5
        self.player.level_down()
        self.assertEqual(self.player.level, 4)
        self.player.level = 1
        self.player.level_down()
        self.assertEqual(self.player.level, 1)


class TestRace(unittest.TestCase):
    def test_race_has_5_cards_on_init(self):
        race = Race()
        result = race.max_cards
        self.assertGreaterEqual(result, 5)

    def test_race_cant_carry_objects_on_init(self):
        race = Race()
        result = race.carry_objects
        self.assertFalse(result)


class TestMunchkin(unittest.TestCase):
    def test_initial_board(self):
        self.muchkin = Munchkin()
        expected_text = "['card1', 'card2']\n"\
                        "Player: name, On Hand: []"
        result_text = self.muchkin.board
        self.assertEquals(expected_text, result_text)


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.my_t_deck = TreasureDeck()
        self.my_d_deck = DoorDeck()

    def test_cards(self):
        self.assertEqual(self.my_t_deck.cards, ["treasurecard1", "treasurecard2", "treasurecard3", "treasurecard4"])
        self.assertEqual(self.my_d_deck.cards, ["doorcard1", "doorcard2", "doorcard3", "doorcard4"])

    def test_discards_cards(self):
        self.assertEqual(self.my_t_deck.discard_cards, [])
        self.assertEqual(self.my_d_deck.discard_cards, [])

    def test_add_discard(self):
        self.my_d_deck.add_discard("ADDED")
        self.my_t_deck.add_discard("ADDED")
        self.assertEqual(self.my_d_deck.discard_cards, ["ADDED"])
        self.assertEqual(self.my_t_deck.discard_cards, ["ADDED"])

    def test_add_cards(self):
        self.my_d_deck.add_cards(["ADDED1E", "ADDED2E"])
        self.my_t_deck.add_cards(["ADDED1", "ADDED2"])
        self.assertEqual(self.my_d_deck.cards, ["doorcard1", "doorcard2", "doorcard3", "doorcard4", "ADDED1E", "ADDED2E"])
        self.assertEqual(self.my_t_deck.cards, ["treasurecard1", "treasurecard2", "treasurecard3", "treasurecard4", "ADDED1", "ADDED2"])

    def test_shuffle_cards(self):
        self.my_d_deck.shuffle_deck()
        self.my_t_deck.shuffle_deck()
        self.assertNotEqual(self.my_d_deck.cards, ["doorcard1", "doorcard2", "doorcard3", "doorcard4"])
        self.assertNotEqual(self.my_t_deck.cards, ["treasurecard1", "treasurecard2", "treasurecard3", "treasurecard4"])

    def test_reset_cards(self):
        self.my_d_deck.add_discard("ADDED1")
        self.my_d_deck.reset_cards()
        self.my_t_deck.add_discard("ADDED1E")
        self.my_t_deck.reset_cards()
        self.assertEqual(self.my_d_deck.cards, ["ADDED1"])
        self.assertEqual(self.my_t_deck.cards, ["ADDED1E"])

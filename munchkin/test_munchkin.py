import unittest
from munchkin.treasures import TREASURE_CARDS
from munchkin.treasures.treasure_single_use import TreasureSingleUse
from munchkin.dice import Dice
from munchkin.player import (
    Player,
    MaxCardsOnHandOutRangeException,
)
from munchkin.doors.monster import Monster
from munchkin.doors.races.race import Race
from munchkin.munchkin import Munchkin
from munchkin.deck import TreasureDeck
from munchkin.deck import DoorDeck
from munchkin.treasures.treasure import Treasure
from munchkin.treasures.weapon import Weapon
from munchkin.treasures.armor import Armor
from munchkin.treasures.footwear import Footwear


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

    def test_validate_max_card_passes(self):
        self.player.max_cards_on_hand = 5
        self.player.on_hand = []
        can_draw = self.player.validate_max_card()
        self.assertTrue(can_draw)

    def test_validate_max_card_raises_exception(self):
        weapon = Weapon("Grande", 2, "Maza Suiza Multiusos", 4, 600)
        self.player.max_cards_on_hand = 1
        self.player.on_hand = [weapon]
        with self.assertRaises(MaxCardsOnHandOutRangeException):
            self.player.validate_max_card()


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

    def test_add_player(self):
        self.munchkin = Munchkin()
        player_name = 'Gaston'
        self.munchkin.add_players(player_name)
        self.assertEqual(len(self.munchkin.players), 1)


    def test_initial_board(self):
        pass

    def test_draw_card(self):
        self.munchkin = Munchkin()
        self.munchkin.add_players('Gaston')
        players = self.munchkin.players

        for player in players:
            if player.name == 'Gaston':
                player.isTurn = True
                test_player = player

        self.munchkin.draw_card()

        self.assertEqual(len(test_player.on_hand), 1)



class TestTreasure(unittest.TestCase):

    def test_treasure_basic_info(self):
        treasure = Treasure("Armadura de Cuero", 1, 200)
        self.assertEqual(treasure.name, "Armadura de Cuero")
        self.assertEqual(treasure.bonus, 1)
        self.assertEqual(treasure.value, 200)
        self.assertEqual(treasure.used_by, None)


class TestArmor(unittest.TestCase):

    def test_armor_basic_info(self):
        armor = Armor("Armadura Llameante", 3, 400)
        self.assertEqual(armor.name, "Armadura Llameante")
        self.assertEqual(armor.bonus, 3)
        self.assertEqual(armor.value, 400)
        self.assertEqual(armor.used_by, None)


class TestWeapon(unittest.TestCase):

    def test_weapon_basic_info(self):
        weapon = Weapon("Grande", 2, "Maza Suiza Multiusos", 4, 600)
        self.assertEqual(weapon.size, "Grande")
        self.assertEqual(weapon.cant_hands, 2)
        self.assertEqual(weapon.bonus, 4)
        self.assertEqual(weapon.name, "Maza Suiza Multiusos")
        self.assertEqual(weapon.value, 600)
        self.assertEqual(weapon.used_by, None)


class TestFootwear(unittest.TestCase):

    def setUp(self):
        pass

    def test_weapon_basic_info(self):
        footwear = Footwear("Maza Suiza Multiusos", 4, 600)
        self.assertEqual(footwear.bonus, 4)
        self.assertEqual(footwear.name, "Maza Suiza Multiusos")
        self.assertEqual(footwear.value, 600)
        self.assertEqual(footwear.used_by, None)


class TestTreasureDeck(unittest.TestCase):
    pass


class TestDoorDeck(unittest.TestCase):
    pass



class TestTreasureSingleUse(unittest.TestCase):
    def test_single_card_level_up_basic_info(self):
        cards_single_use = TREASURE_CARDS['single_use']
        single_use_lvl_up = TreasureSingleUse(**cards_single_use[0])
        self.assertEqual(single_use_lvl_up.name, "Matar al escudero")
        self.assertEqual(single_use_lvl_up.bonus, None)
        self.assertEqual(single_use_lvl_up.value, None)
        self.assertFalse(single_use_lvl_up.group_effect)
        self.assertTrue(single_use_lvl_up.is_level_up)
        self.assertTrue(single_use_lvl_up.is_level_up)

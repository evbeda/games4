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
from munchkin.treasures.headwear import Headwear


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
        self.assertFalse(treasure.is_big)


class TestArmor(unittest.TestCase):

    def test_armor_basic_info(self):
        armor = Armor("Armadura Llameante", 3, 400)
        self.assertEqual(armor.name, "Armadura Llameante")
        self.assertEqual(armor.bonus, 3)
        self.assertEqual(armor.value, 400)
        self.assertEqual(armor.used_by, None)
        self.assertFalse(armor.is_big)


class TestWeapon(unittest.TestCase):

    def test_weapon_basic_info(self):
        weapon = Weapon(2, "Maza Suiza Multiusos", 4, 600)
        self.assertEqual(weapon.cant_hands, 2)
        self.assertEqual(weapon.bonus, 4)
        self.assertEqual(weapon.name, "Maza Suiza Multiusos")
        self.assertEqual(weapon.value, 600)
        self.assertEqual(weapon.used_by, None)
        self.assertFalse(weapon.is_big)


class TestFootwear(unittest.TestCase):

    def test_footwear_basic_info(self):
        footwear = Footwear("Maza Suiza Multiusos", 4, 600)
        self.assertEqual(footwear.bonus, 4)
        self.assertEqual(footwear.name, "Maza Suiza Multiusos")
        self.assertEqual(footwear.value, 600)
        self.assertEqual(footwear.used_by, None)
        self.assertFalse(footwear.is_big)

class TestHeadwear(unittest.TestCase):

    def test_headwear_basic_info(self):
        headwear = Headwear("Pañuelo para tipos duros", 3, 400)
        self.assertEqual(headwear.bonus, 3)
        self.assertEqual(headwear.name, "Pañuelo para tipos duros")
        self.assertEqual(headwear.value, 400)
        self.assertEqual(headwear.used_by, None)
        self.assertFalse(headwear.is_big)

class TestTreasureDeck(unittest.TestCase):
    pass


class TestDoorDeck(unittest.TestCase):
    pass


class TestCardMunchkin(unittest.TestCase):
    def setUp(self):
        self.treasure = Treasure()
        self.weapon = Weapon("Axe", 2, 1, 600, "Human")
        self.armor = Armor("Armadura de cuero", 1, "Armadura", 200, "Male")
        self.headwear = Headwear("Yelmo cornudo", 1, 600, "all", extra_bonus = 2, extra_used_by = "Elf")

    def test_abstract_Card(self):
        self.assertIsNone(self.treasure.type_treasure)
        self.assertEqual(self.treasure.type, "Treasure")

    def test_weapon_card(self):
        self.assertEqual(self.weapon.type, "Treasure")
        self.assertEqual(self.weapon.type_treasure, "Weapon")
        self.assertEqual(self.weapon.name, "Axe")

        # Level to fight against the monster
        self.assertEqual(self.weapon.bonus, 2)

        # Cant_hands of Weapon, use 1 or 2 values, it can used with 1 hand of both
        self.assertEqual(self.weapon.cant_hands, 1)

        # Value to sell the weapon, if the player get 1000 in two weapons, he can sell it for +1 Level!
        self.assertEqual(self.weapon.value, 600)

        # Some Weapons can be used by some Races, or some class, when get "All" means what it can use for everyone
        self.assertEqual(self.weapon.used_by, "Human")

    def test_headwear_card(self):
        self.assertEqual(self.headwear.type, "Treasure")
        self.assertEqual(self.headwear.type_treasure, "Headwear")
        self.assertEqual(self.headwear.name, "Yelmo cornudo")

        # Level to fight against the monster
        self.assertEqual(self.headwear.bonus, 1)

        # Value to sell the weapon, if the player get 1000 in two weapons, he can sell it for +1 Level!
        self.assertEqual(self.headwear.value, 600)

        # Some Weapons can be used by some Races, or some class, when get "All" means what it can use for everyone
        self.assertEqual(self.headwear.used_by, "all")

        # A special headwear gives you +2 if you are elf!
        self.assertEqual(self.headwear.extra_bonus, 2)

        # A special headwear gives you +2 if you are elf!
        self.assertEqual(self.headwear.extra_used_by, "Elf")



    def test_armor_card(self):
        self.assertEqual(self.armor.type, "Treasure")
        self.assertEqual(self.armor.type_treasure, "Armor")
        self.assertEqual(self.armor.name, "Armadura de cuero")

        # Level to fight against the monster
        self.assertEqual(self.armor.bonus, 1)

        # Value to sell the armor, if the player get 1000 in two armors, he can sell it for +1 Level!
        self.assertEqual(self.armor.value, 200)
        # Part of armor, use armadura, armadura grande, calzado , etc
        self.assertEqual(self.armor.part, "Armadura")
        # Some armors can be used by some Races, or some class, when get "All" means what it can use for everyone
        self.assertEqual(self.armor.used_by, "Male")


class TestTreasureSingleUse(unittest.TestCase):
    def test_single_card_level_up_basic_info(self):
        cards_single_use = TREASURE_CARDS['single_use']
        single_use_lvl_up = TreasureSingleUse(**cards_single_use[0])
        self.assertEqual(single_use_lvl_up.name, "Matar al escudero")
        self.assertEqual(single_use_lvl_up.bonus, None)
        self.assertEqual(single_use_lvl_up.value, None)
        self.assertFalse(single_use_lvl_up.group_effect)
        self.assertTrue(single_use_lvl_up.is_level_up)
        self.assertFalse(single_use_lvl_up.reroll_dice)

    def test_single_card_raise_fight_power(self):
        cards_single_use = TREASURE_CARDS['single_use']
        raise_fight_power = TreasureSingleUse(**cards_single_use[1])
        self.assertEqual(raise_fight_power.name, "Globitos de colores")
        self.assertEqual(raise_fight_power.bonus, 5)
        self.assertEqual(raise_fight_power.value, None)
        self.assertFalse(raise_fight_power.group_effect)
        self.assertFalse(raise_fight_power.is_level_up)

    def test_single_card_reroll_dice(self):
        cards_single_use = TREASURE_CARDS['single_use']
        reroll_dice = TreasureSingleUse(**cards_single_use[2])
        self.assertEqual(reroll_dice.name, "Frasco de pegamento")
        self.assertEqual(reroll_dice.bonus, None)
        self.assertEqual(reroll_dice.value, 100)
        self.assertFalse(reroll_dice.group_effect)
        self.assertFalse(reroll_dice.is_level_up)
        self.assertTrue(reroll_dice.reroll_dice)

    def test_single_card_flee(self):
        cards_single_use = TREASURE_CARDS['single_use']
        flee = TreasureSingleUse(**cards_single_use[3])
        self.assertEqual(flee.name, "Muro instantaneo")
        self.assertEqual(flee.bonus, None)
        self.assertEqual(flee.value, 300)
        self.assertFalse(flee.group_effect)
        self.assertFalse(flee.is_level_up)
        self.assertFalse(flee.reroll_dice)
        self.assertEqual(flee.flee_points, 5)

    def test_single_win_treasure(self):
        cards_single_use = TREASURE_CARDS['single_use']
        treasure_single_use = TreasureSingleUse(**cards_single_use[4])
        self.assertEqual(treasure_single_use.name, "Pocion de amistad")
        self.assertEqual(treasure_single_use.bonus, 99)
        self.assertEqual(treasure_single_use.value, 200)
        self.assertTrue(treasure_single_use.group_effect)
        self.assertFalse(treasure_single_use.is_level_up)
        self.assertFalse(treasure_single_use.reroll_dice)
        self.assertEqual(treasure_single_use.flee_points, 0)
        self.assertFalse(treasure_single_use.win_treasure)



import unittest
from unittest.mock import patch

from munchkin.doors.door import Door
from munchkin.treasures import TREASURE_CARDS
from munchkin.treasures.treasure_single_use import TreasureSingleUse
from munchkin.player import (
    Player,
    MaxCardsOnHandOutRangeException,
)
from munchkin.doors.monster import Monster
from munchkin.doors.races.race import Race
from munchkin.munchkin import Munchkin
from munchkin.deck import Deck
from munchkin.deck import TreasureDeck
from munchkin.deck import DoorDeck
from munchkin.treasures.treasure import Treasure
from munchkin.treasures.various import Various
from munchkin.treasures.weapon import Weapon
from munchkin.treasures.armor import Armor
from munchkin.treasures.footwear import Footwear
from munchkin.treasures.headwear import Headwear
from munchkin.treasures.accessories import Accessories


class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster = Monster("CHUPACABRAS", 8, 1, 2)

    def test_monster_name(self):
        self.assertEqual(self.monster.name, "CHUPACABRAS")

    def test_monster_has_power_greater_or_equal_than_1(self):
        result = self.monster.power
        self.assertGreaterEqual(result, 1)

    def test_monster_has_treasures_greater_or_equal_than_1(self):
        result = self.monster.treasures
        self.assertGreaterEqual(result, 1)

    def test_monster_has_level_add_greater_or_equal_than_1(self):
        result = self.monster.level_add
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 9)

    def test_monster_defeated_true(self):
        player = Player("Rulo")
        treasure_deck = TreasureDeck()
        player.level = 9
        self.assertTrue(self.monster.monster_defeated(player, treasure_deck))

    def test_monster_defeated_false(self):
        player = Player("Rulo")
        treasure_deck = TreasureDeck()
        player.level = 7
        self.assertFalse(self.monster.monster_defeated(player, treasure_deck))


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

    def test_set_default_status(self):
        self.player.name = "changed"
        self.player.level = 4
        self.player.on_hand = ["card"]
        self.player.on_board = ["card"]
        self.player.max_class_cards = 2
        self.player.fleeing_chance = -2
        self.player.max_race_cards = 2
        self.player.max_cards_on_hand = 7
        self.player.set_default_status()
        self.assertEqual(self.player.name, "changed")
        self.assertEqual(self.player.level, 4)
        self.assertEqual(self.player.on_hand, ["card"])
        self.assertEqual(self.player.on_board, ["card"])
        self.assertEqual(self.player.max_race_cards, 1)
        self.assertEqual(self.player.max_class_cards, 1)
        self.assertEqual(self.player.max_cards_on_hand, 5)
        self.assertEqual(self.player.fleeing_chance, -4)

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

    def test_player_str(self):
        armor = Armor("Armadura Llameante", 3, 400)
        self.player.on_hand = [armor]
        self.assertEqual(self.player.__str__(), "Player: person \n On Hand: Name: Armadura Llameante | Bonus: 3 | Value: 400 | Used by: all | Is big?: False | ")

    def test_player_win_true(self):
        self.player.level = 10
        result = self.player.win()
        self.assertTrue(result)

    def test_player_win_fales(self):
        result = self.player.win()
        self.assertFalse(result)


class TestRace(unittest.TestCase):
    def setUp(self):
        self.race = Race()

    def test_race_has_5_cards_on_init(self):
        result = self.race.max_cards
        self.assertGreaterEqual(result, 5)

    def test_race_cant_carry_objects_on_init(self):
        result = self.race.carry_objects
        self.assertFalse(result)

    def test_race_max_cards_setter(self):
        number_of_cards = 3
        self.race.max_cards = 3
        self.assertEqual(number_of_cards, self.race.max_cards)

    def test_carry_objects_setter(self):
        self.race.carry_objects = True
        self.assertTrue(self.race.carry_objects)


class TestMunchkin(unittest.TestCase):

    def setUp(self):
        self.munchkin = Munchkin()
        self.player_1 = self.munchkin.players[0]
        self.player_2 = self.munchkin.players[1]
        self.door_deck = self.munchkin.door_deck
        self.treasure_deck = self.munchkin.treasure_deck

    def test_munchkin_initialization(self):
        self.assertEqual(len(self.munchkin.players), 2)
        self.assertEqual(len(self.player_1.on_hand), 4)
        self.assertEqual(len(self.player_2.on_hand), 4)
        self.assertIsNotNone(self.door_deck)
        self.assertIsNotNone(self.treasure_deck)
        self.assertEqual(self.munchkin.current_player, self.player_1)

    def test_draw_card(self):
        self.munchkin.draw_card()
        self.assertEqual(len(self.player_1.on_hand), 5)

    def test_munchkin_board(self):
        card = Armor("Armadura Llameante", 3, 400)
        self.player_1.on_board = [card]
        expected = "Name: 1\nCards on Board:\nName: Armadura Llameante | Bonus: 3 | Value: 400 | Used by: all | Is big?: False | \n"\
            "Name: 2\nCards on Board:\n"
        result = self.munchkin.board
        self.assertEqual(result, expected)

    def test_munchkin_play_defeat_monster(self):
        self.player_1.level = 9
        self.munchkin.current_card = Monster('Rey Tut', 8, 4, 2)
        result = self.munchkin.play()
        expected = "You defetead the monster"
        self.assertEqual(result, expected)
        self.assertEqual(self.player_1.level, 11)

    @patch(
        'munchkin.munchkin.random.randint',
        return_value=2
    )
    def test_munchkin_play_dice_lose(self, patch_dice):
        self.player_1.level = 7
        self.munchkin.current_card = Monster('Rey Tut', 8, 4, 2)
        self.assertEqual(self.munchkin.play(), "You're lose")

    @patch(
        'munchkin.munchkin.random.randint',
        return_value=6
    )
    def test_munchkin_play_dice_safe(self, patch_dice):
        self.player_1.level = 7
        self.munchkin.current_card = Monster('Rey Tut', 8, 4, 2)
        self.assertEqual(self.munchkin.play(), "You're safe")

    def test_next_turn(self):
        result = 'Is your turn: 1\n' \
                 'Card: Name: Armadura Llameante |' \
                 ' Bonus: 3 | Value: 400 |' \
                 ' Used by: Elfs |' \
                 ' Is big?: False | '
        self.munchkin.current_card = Armor("Armadura Llameante", 3, 400, "Elfs")
        self.assertEqual(self.munchkin.next_turn(), result)


class TestTreasure(unittest.TestCase):

    def test_treasure_basic_info(self):
        treasure = Treasure("Armadura de Cuero", 1, 200)
        self.assertEqual(treasure.name, "Armadura de Cuero")
        self.assertEqual(treasure.bonus, 1)
        self.assertEqual(treasure.value, 200)
        self.assertEqual(treasure.used_by, None)
        self.assertFalse(treasure.is_big)

    def test_treasure_str(self):
        treasure = Treasure("Armadura de Cuero", 1, 200, "Elfs")
        self.assertEqual(treasure.__str__(), "Name: Armadura de Cuero | Bonus: 1 | Value: 200 | Used by: Elfs | Is big?: False | ")


class TestArmor(unittest.TestCase):

    def test_armor_basic_info(self):
        armor = Armor("Armadura Llameante", 3, 400)
        self.assertEqual(armor.name, "Armadura Llameante")
        self.assertEqual(armor.bonus, 3)
        self.assertEqual(armor.value, 400)
        self.assertEqual(armor.used_by, None)
        self.assertFalse(armor.is_big)

    def test_armor_str(self):
        armor = Armor("Armadura Llameante", 3, 400, "Elfs")
        self.assertEquals(armor.__str__(), "Name: Armadura Llameante | Bonus: 3 | Value: 400 | Used by: Elfs | Is big?: False | ")


class TestWeapon(unittest.TestCase):

    def test_weapon_basic_info(self):
        weapon = Weapon(2, "Maza Suiza Multiusos", 4, 600)
        self.assertEqual(weapon.cant_hands, 2)
        self.assertEqual(weapon.bonus, 4)
        self.assertEqual(weapon.name, "Maza Suiza Multiusos")
        self.assertEqual(weapon.value, 600)
        self.assertEqual(weapon.used_by, None)
        self.assertFalse(weapon.is_big)

    def test_weapon_str(self):
        weapon = Weapon(2, "Maza Suiza Multiusos", 4, 600)
        self.assertEqual(weapon.__str__(), "Name: Maza Suiza Multiusos | Bonus: 4 | Value: 600 | Used by: all | Is big?: False | Cant hands: 2 | ")


class TestFootwear(unittest.TestCase):

    def test_footwear_basic_info(self):
        footwear = Footwear("Maza Suiza Multiusos", 4, 600)
        self.assertEqual(footwear.bonus, 4)
        self.assertEqual(footwear.name, "Maza Suiza Multiusos")
        self.assertEqual(footwear.value, 600)
        self.assertEqual(footwear.used_by, None)
        self.assertFalse(footwear.is_big)

    def test_footwear_str(self):
        footwear = Footwear("Maza Suiza Multiusos", 4, 600)
        self.assertEquals(footwear.__str__(), "Name: Maza Suiza Multiusos | Bonus: 4 | Value: 600 | Used by: all | Is big?: False | Flee bonus: 0 | ")


class TestHeadwear(unittest.TestCase):

    def test_headwear_basic_info(self):
        headwear = Headwear("Pañuelo para tipos duros", 3, 400)
        self.assertEqual(headwear.bonus, 3)
        self.assertEqual(headwear.name, "Pañuelo para tipos duros")
        self.assertEqual(headwear.value, 400)
        self.assertEqual(headwear.used_by, None)
        self.assertFalse(headwear.is_big)

    def test_headwear_str(self):
        headwear = Headwear("Pañuelo para tipos duros", 3, 400)
        self.assertEqual(headwear.__str__(), "Name: Pañuelo para tipos duros | Bonus: 3 | Value: 400 | Used by: all | Is big?: False | Extra bonus: 0 | Extra used by: Nobody | ")


class TestAccesories(unittest.TestCase):

    def test_accessories_basic_info(self):
        accessories = Accessories("Capa de Sombras", 4, 600)
        self.assertEqual(accessories.bonus, 4)
        self.assertEqual(accessories.name, "Capa de Sombras")
        self.assertEqual(accessories.value, 600)
        self.assertEqual(accessories.used_by, None)
        self.assertFalse(accessories.is_big)

    def test_accessories_str(self):
        accessories = Accessories("Capa de Sombras", 4, 600)
        self.assertEqual(accessories.__str__(), "Name: Capa de Sombras | Bonus: 4 | Value: 600 | Used by: all | Is big?: False | ")


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.treasure = Treasure("treasure", 0, 0)

    def test_add_discard_cards(self):
        self.deck.add_discard(self.treasure)
        self.assertEqual(len(self.deck.discard_cards), 1)

    def test_reset_cards(self):
        self.deck.add_discard(self.treasure)
        self.deck.reset_cards()
        self.assertNotEqual(self.deck.cards, [])
        self.assertEqual(self.deck.discard_cards, [])


class TestTreasureDeck(unittest.TestCase):

    def setUp(self):
        self.treasure_deck = TreasureDeck()

    def test_treasure_deck_not_none(self):
        self.assertIsNotNone(self.treasure_deck)

    def test_len_treasure_deck(self):
        '''
            Por Ahora hay esta cantidad de cartas de treasure, este metodo prueba que el len funcione,
            actualizar el nro de cartas a medida que se vayan agregando nuevas
        '''
        self.assertEqual(len(self.treasure_deck), 67)

    def test_treasure_deck_check_every_card_has_attributes_not_none(self):
        for treasure_card in self.treasure_deck.cards:
            self.assertIsNotNone(treasure_card.name)
            self.assertIsNotNone(treasure_card.bonus)
            self.assertIsNotNone(treasure_card.is_big)
            self.assertIsNotNone(treasure_card.used_by)


class TestDoor(unittest.TestCase):
    def test_door_name(self):
        door = Door('Chupacabras')
        self.assertEqual(door.__str__(), 'Name: '+door.name)


class TestDoorDeck(unittest.TestCase):
    def setUp(self):
        self.door_deck = DoorDeck()

    def test_treasure_deck_not_none(self):
        self.assertIsNotNone(self.door_deck)

    def test_len_treasure_deck(self):
        '''
            Por Ahora hay esta cantidad de cartas de door, este metodo prueba que el len funcione,
            actualizar el nro de cartas a medida que se vayan agregando nuevas
        '''
        self.assertEqual(len(self.door_deck), 5)


class TestCardMunchkin(unittest.TestCase):
    def setUp(self):
        self.treasure = Treasure("treasure", 0, 0)
        self.door = Door("door")
        self.weapon = Weapon(1, "Axe", 2, 600, "Human")
        self.armor = Armor("Armadura de cuero", 1, 200, "Male")
        self.headwear = Headwear("Yelmo cornudo", 1, 600, "all", extra_bonus=2, extra_used_by="Elf")
        self.accessories = Accessories("Capa de Sombras", 4, 600, "thief")
        self.various = Various("Escalera", 3, 400, "Halfling", True, 0, 2)

    def test_abstract_Card(self):
        self.assertEqual(type(self.treasure).__name__, "Treasure")
        self.assertEqual(type(self.door).__name__, "Door")

    def test_weapon_card(self):
        self.assertTrue(isinstance(self.weapon, Weapon))
        self.assertEqual(type(self.weapon).__name__, "Weapon")
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
        self.assertTrue(isinstance(self.headwear, Treasure))
        self.assertEqual(type(self.headwear).__name__, "Headwear")
        self.assertEqual(self.headwear.name, "Yelmo cornudo")

        # Level to fight against the monster
        self.assertEqual(self.headwear.bonus, 1)

        # Value to sell the item, if the player get 1000 in two items, he can sell it for +1 Level!
        self.assertEqual(self.headwear.value, 600)

        # Some Headwear can be used by some Races, or some class, when get "All" means what it can use for everyone
        self.assertEqual(self.headwear.used_by, "all")

        # A special headwear gives you +2 if you are elf!
        self.assertEqual(self.headwear.extra_bonus, 2)

        # A special headwear gives you +2 if you are elf!
        self.assertEqual(self.headwear.extra_used_by, "Elf")

    def test_armor_card(self):
        self.assertTrue(isinstance(self.armor, Treasure))
        self.assertEqual(type(self.armor).__name__, "Armor")
        self.assertEqual(self.armor.name, "Armadura de cuero")

        # Level to fight against the monster
        self.assertEqual(self.armor.bonus, 1)

        # Value to sell the armor, if the player get 1000 in two armors, he can sell it for +1 Level!
        self.assertEqual(self.armor.value, 200)

        # Some armors can be used by some Races, or some class, when get "All" means what it can use for everyone
        self.assertEqual(self.armor.used_by, "Male")

    def test_various_card(self):
        self.assertEqual(self.various.name, "Escalera")
        self.assertEqual(self.various.bonus, 3)
        self.assertEqual(self.various.value, 400)
        self.assertEqual(self.various.used_by, "Halfling")
        self.assertEqual(self.various.is_big, True)
        self.assertEqual(self.various.cant_hand, 2)

    def test_accessories_card(self):
        self.assertEqual(self.accessories.name, "Capa de Sombras")

        # Level to fight against the monster
        self.assertEqual(self.accessories.bonus, 4)

        # Value to sell the item, if the player get 1000 in two items, he can sell it for +1 Level!
        self.assertEqual(self.accessories.value, 600)

        # Some items can be used by some Races, or some class, when get "All" means what it can use for everyone
        self.assertEqual(self.accessories.used_by, "thief")

    def test_various_str(self):
        self.assertEqual(self.various.__str__(), "Name: Escalera | Bonus: 3 | Value: 400 | Used by: Halfling | Is big?: True | Flee bonus: 0 | Cant Hand: 2 | ")


class TestTreasureSingleUse(unittest.TestCase):
    def test_single_card_level_up_basic_info(self):
        cards_single_use = TREASURE_CARDS['single_use']
        single_use_lvl_up = TreasureSingleUse(**cards_single_use[0])
        self.assertEqual(single_use_lvl_up.name, "Matar al escudero")
        self.assertEqual(single_use_lvl_up.bonus, 0)
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
        self.assertEqual(reroll_dice.bonus, 0)
        self.assertEqual(reroll_dice.value, 100)
        self.assertFalse(reroll_dice.group_effect)
        self.assertFalse(reroll_dice.is_level_up)
        self.assertTrue(reroll_dice.reroll_dice)

    def test_single_card_flee(self):
        cards_single_use = TREASURE_CARDS['single_use']
        flee = TreasureSingleUse(**cards_single_use[3])
        self.assertEqual(flee.name, "Muro instantaneo")
        self.assertEqual(flee.bonus, 0)
        self.assertEqual(flee.value, 300)
        self.assertFalse(flee.group_effect)
        self.assertFalse(flee.is_level_up)
        self.assertFalse(flee.reroll_dice)
        self.assertEqual(flee.flee_points, 5)

    def test_single_card_win_treasure(self):
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

    def test_single_card_affect_other_player(self):
        cards_single_use = TREASURE_CARDS['single_use']
        treasure_single_use = TreasureSingleUse(**cards_single_use[5])
        self.assertEqual(treasure_single_use.name, "Pocion de transferencia")
        self.assertEqual(treasure_single_use.bonus, 0)
        self.assertEqual(treasure_single_use.value, 300)
        self.assertFalse(treasure_single_use.group_effect)
        self.assertFalse(treasure_single_use.is_level_up)
        self.assertFalse(treasure_single_use.reroll_dice)
        self.assertEqual(treasure_single_use.flee_points, 0)
        self.assertTrue(treasure_single_use.win_treasure)
        self.assertTrue(treasure_single_use.affect_other_player)

    def test_single_use_str(self):
        cards_single_use = TREASURE_CARDS['single_use']
        single_use_lvl_up = TreasureSingleUse(**cards_single_use[0])
        self.assertEqual(single_use_lvl_up.__str__(), "Name: Matar al escudero | Bonus: 0 | Value: 0 | Used by: all | Is big?: False | Group effect: False | Is level up: True | Re-roll dice: False | Flee points: 0 | Win treasure: True | Affect other player: False | ")

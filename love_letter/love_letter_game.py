from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer


class TargetMyselfException(Exception):
    pass


class TargetInvalidException(Exception):
    pass


hearts_to_win = {
    # number_of_players: hearts_to_win

    2: 7,
    3: 5,
    4: 4,
}


class LoveLetterGame:

    def __init__(self, name):
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.players = [HumanPlayer(name, self), PcPlayer(self)]
        # Logica de sacar cartas (regla del juego para 2 jugadores)
        if len(self.players) == 2:
            self.deck.remove_last()
            self.deck.show_three()

        for player in self.players:
            card = self.deck.draw_card()
            player.draw_card(card)

        self.current_player = self.players[0]

    def next_turn(self):
        text = ""
        if self.current_player.is_active:
            for index in range(len(self.current_player.cards)):
                text += str(index) + "-" + \
                        self.current_player.cards[index].__str__() + "\n"
        return "Its your turn\n" + text

    def play(self, command):
        commands = command.split("-")
        command_args = []
        if len(commands) > 1:
            command_args.append(self.players[int(commands[1])])
            try:
                self.validate_effect(self.players[int(commands[1])])
            except Exception as e:
                return e.message
        command_args.extend(commands[2:])
        self.current_player.cards[int(commands[0])].execute_action(*command_args)
        self.give_heart()

        # lo que ingreso el usuario por input (puede ser mas de un valor)
        # return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win

    def validate_effect(self, player):
        if not player.is_active:
            raise TargetInvalidException(
                'Player {} is not active'.format(player.name)
            )

        if player in self.look_for_handmaid():
            raise TargetInvalidException(
                'Player {} has handmaid activated'.format(player.name)
            )
        return True

    def give_heart(self):
        alive = {}
        for player in self.players:
            if player.is_active:
                alive[player.name] = player.show_card().score
        if len(alive) == 1:

            alive_name = lambda x: x[0]
            for player in self.players:
                if player.name == alive_name:
                    player.hearts += 1
            return True
        if len(self.deck.cards) == 0:
            items_max_value = max(alive.items(), key=lambda x: x[1])
            list_of_winners = list()
            for key, value in alive.items():
                if value == items_max_value[1]:
                    list_of_winners.append(key)
            if len(list_of_winners) == 1:
                for player in self.players:
                    if player.name == list_of_winners[0]:
                        player.hearts += 1
                        return True
            else:
                max_score = 0
                winner_player = None
                for player in self.players:
                    for winner in list_of_winners:
                        if player.name == winner and player.score > max_score:
                            max_score = player.score
                            winner_player = player
                winner_player.hearts += 1
                return True
        return False

    def look_for_handmaid(self):
        save_players = []
        for player in self.players:
            if (
                    len(player.discarded) > 0 and
                    player.discarded[0].name == "Handmaid"
            ):
                save_players.append(player)
        return save_players

    @property
    def board(self):
        text_to_show = "{}".format(self.deck.__str__())
        for player in self.players:
            text_to_show += "\n{}".format(player.__str__())
        # -> muestra al usuario el estado actual
        # del juego (no del feedback de lo que acaba de hacer)
        return text_to_show

    def reset_round(self):
        for player in self.players:
            player.reset_round()

    def check_winner(self):
        return len([player for player in self.players if player.hearts == hearts_to_win[len(self.players)]]) > 0

    def get_opponents(self):
        players_duplicate = self.players.copy()
        players_duplicate.remove(self.current_player)
        return players_duplicate

    def select_target(self, player_name):
        if player_name == self.current_player.name:
            raise TargetMyselfException()
        for player in self.players:
            if player.name == player_name:
                return player

    def get_deck_card(self):
        return self.deck.draw_card()

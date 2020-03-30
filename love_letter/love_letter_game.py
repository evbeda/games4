from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer


class TargetMyselfException(Exception):
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
                text += str(index) + "-" + self.current_player.cards[index].__str__() + "\n"
        return "Its your turn\n" + text

    def play(self, command):
        commands = command.split("-")
        if len(commands) == 1:
            return self.current_player.cards[int(commands[0])].execute_action()
        if len(commands) == 2:
            return self.current_player.cards[int(commands[0])].execute_action(self.players[int(commands[1])])
        if len(commands) == 3:
            return self.current_player.cards[int(commands[0])].execute_action(self.players[int(commands[1])],commands[2])    
        #lo que ingreso el usuario por input (puede ser mas de un valor)
        # return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win

    @property
    def board(self):
        text_to_show = "{}".format(self.deck.__str__())
        for player in self.players:
            text_to_show+="\n{}".format(player.__str__())
        return text_to_show #-> muestra al usuario el estado actual del juego (no del feedback de lo que acaba de hacer)

    def end_of_round(self):
        for player in self.players:
            player.end_of_round()

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

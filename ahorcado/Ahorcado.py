class Ahorcado:

	is_win = False

	def __init__(self):
		self.word = self.get_word_from_api()
		self.lifes = 6
		self.status_message = "Welcome to the game! Please choose one letter"
		self.hidden_letters_message = "_ _ _ _ _ _ _ "
		self.used_letters_message = ""
		self.lifes_message = "Lifes: {}".format(self.lifes)

	def get_word_from_api(self):
		return "palabra"

	def play(self, letter):
		if letter not in self.word:
			self.lifes = self.lifes - 1
			self.status_message = "Wrong letter, you lose one life"
		elif letter in self.word:
			self.status_message = "Correct letter! Choose another"
            self.is_win = True

	def show_board(self):
		return self.status_message + '\n' + self.hidden_letters_message + '\n' + self.used_letters_message + '\n' + self.lifes_message

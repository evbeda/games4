class Ahorcado:

	is_win = False

	def __init__(self):
		self.word = self.get_word_from_api()
		self.lifes = 6
		self.status_message = ""

	def get_word_from_api(self):
		return "palabra"

	def play(self, letter):
		if letter not in self.word:
			self.lifes = self.lifes - 1
			self.status_message = "Wrong letter, you lose one life"
		elif letter in self.word:
			self.status_message = "Right letter! Choose another"
			self.is_win = True


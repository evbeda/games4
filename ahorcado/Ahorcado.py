class Ahorcado:

	is_win = False

	def __init__(self):
		self.word = self.get_word()

	def get_word(self):
		return "palabra"

	def play(self, word):
		self.is_win = True


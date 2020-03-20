class Ahorcado:

	def __init__(self):
		self.word = self.get_word_from_api()
		self.lifes = 6
		self.used_letters = []

	def next_turn(self):
		if not self.check_is_playing() and self.lifes > 0:
			return "The player already won"
		elif not self.check_is_playing() and self.lifes == 0:
			return "The player already lost"
		else:
			return "Please input a letter from A-Z"

	def play(self, letter):
		if self.check_input_used_letters(letter):
			return "Already tried that Letter! Try again"
			
		elif not self.check_input_word(letter):
			self.lifes = self.lifes - 1
			self.set_used_letters(letter)
			return "Wrong letter, you lose one life"

		elif self.check_input_word(letter):
			self.set_used_letters(letter)
			return "Correct letter! Choose another"

	def get_lifes(self):
		return "Lifes: {}".format(self.lifes)

	def get_word_from_api(self):
		return "palabra"

	def set_used_letters(self, letter):
		if letter not in self.used_letters:
			self.used_letters.append(letter)
		else:
			pass

	def check_input_used_letters(self, letter):
		if letter in self.used_letters:
			return True
		else:
			return False
	
	def check_input_word(self, letter):
		if letter in self.word:
			return True
		else:
			return False

	def check_is_playing(self):
		if self.lifes > 0 and "_" not in self.hidden_letters_message():
			return False
		if self.lifes > 0:
			return True
		elif self.lifes == 0:
			return False

	def hidden_letters_message(self):
		new_hidden_letters = []
		for character in self.word:
			if character in self.used_letters:
				new_hidden_letters.append(character)
			elif character not in self.used_letters:
				new_hidden_letters.append("_")
		return " ".join(new_hidden_letters)

	@property
	def board(self):
		return  self.hidden_letters_message() + '\n' + " ".join(self.used_letters) + '\n' + self.get_lifes()


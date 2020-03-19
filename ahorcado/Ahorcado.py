class Ahorcado:

	def __init__(self):
		self.word = self.get_word_from_api()
		self.lifes = 6
		self.is_win = False
		self.is_lose = False

		self.status = "Welcome to the game! Please choose one letter"
		#self.hidden_letters_message = "_ _ _ _ _ _ _"
		self.used_letters = []
		self.lifes_message = "Lifes: {}".format(self.lifes)

	def get_word_from_api(self):
		return "palabra"

	def status_message(self):
		return self.status_message

	def hidden_letters_message(self):
		new_hidden_letters = []
		for character in self.word:
			if character in self.used_letters:
				new_hidden_letters.append(character)
			elif character not in self.used_letters:
				new_hidden_letters.append("_")
		return " ".join(new_hidden_letters)

	def next_turn(self):
		if self.is_win:
			self.status = "The player already won"
			return "The player already won"
		elif self.is_lose:
			self.status = "The player already lost"
			return "The player already lost"
		return "Please input a letter from A-Z"

	def play(self, letter):
		if self.check_input(letter):
			self.status = "Already tried that Letter! Try again"
			
		elif not self.check_input_word(letter):
			self.lifes = self.lifes - 1
			self.status = "Wrong letter, you lose one life"
			self.set_used_letters(letter)
			
		elif self.check_input_word(letter):
			self.status = "Correct letter! Choose another"
			self.set_used_letters(letter)
		
		self.next_turn()
	
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

	def set_used_letters(self, letter):
		if letter not in self.used_letters:
			self.used_letters.append(letter)
		else:
			pass


	@property
	def board(self):
		return self.status + '\n' + self.hidden_letters_message() + '\n' + " ".join(self.used_letters) + '\n' + self.lifes_message

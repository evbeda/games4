class Ahorcado:

	def __init__(self):
		self.word = self.get_word_from_api()
		self.lifes = 6
		self.is_win = False
		self.is_lose = False

		self.status_message = "Welcome to the game! Please choose one letter"
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
			elif character not in self.used_letters_message:
				new_hidden_letters.append("_")
		return " ".join(new_hidden_letters)

	def next_turn(self):
		if self.is_win:
			self.status_message = "The player already won"
			return "The player already won"
		elif self.is_lose:
			self.status_message = "The player already lost"
			return "The player already lost"
		else:
			#print(self.board)
			in_letter = input("Please, put letter: ")
			self.play(in_letter)

	def play(self, letter):
		if letter in self.used_letters:
			self.status_message = "Already tried that Letter! Try again"
			self.next_turn()
		elif letter not in self.word:
			self.lifes = self.lifes - 1
			self.status_message = "Wrong letter, you lose one life"
			self.set_used_letters(letter)
			self.next_turn()
		elif letter in self.word:
			self.status_message = "Correct letter! Choose another"
			self.set_used_letters(letter)
			self.next_turn()

	def set_used_letters(self, letter):
		if letter not in used_letters:
			self.used_letters.append(letter)
		else:
			pass


	@property
	def board(self):
		return self.status_message + '\n' + self.hidden_letters_message() + '\n' + self.used_letters_message + '\n' + self.lifes_message

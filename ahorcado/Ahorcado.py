class Ahorcado:

	is_win = False
	is_lose = False

	def __init__(self):
		self.word = self.get_word_from_api()
		self.lifes = 6
		self.status_message = "Welcome to the game! Please choose one letter"
		self.hidden_letters_message = "_ _ _ _ _ _ _"
		self.used_letters_message = ""
		self.lifes_message = "Lifes: {}".format(self.lifes)

	def get_word_from_api(self):
		return "palabra"

	def next_turn(self):
		if is_win:
			self.status_message = "The player already won"
			return "The player already won"
		elif is_lose:
			self.status_message = "The player already lost"
			return "The player already lost"
		else:
			self.show_board()
			self.play()

	def play(self, letter):
		if letter in self.used_letters_message:
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
			self.set_hidden_letters(letter)
			
			
			self.next_turn()

	def set_hidden_letters(self, letter):
		word = list(self.word)
		new_hidden_letters = []
		for character in word:
			if letter == character:
				new_hidden_letters.append(letter)
			elif letter != character and character == "_":
				new_hidden_letters.append("_")
			else:
				new_hidden_letters.append(character)
		self.hidden_letters_message = " ".join(new_hidden_letters)

	def set_used_letters(self, letter):
		self.used_letters_message += letter + " "

	def show_board(self):
		return self.status_message + '\n' + self.hidden_letters_message + '\n' + self.used_letters_message + '\n' + self.lifes_message

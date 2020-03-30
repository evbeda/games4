class Cell:

	def __init__(self):
		self.token = None

	@property
	def is_empty(self):
		return self.token is None

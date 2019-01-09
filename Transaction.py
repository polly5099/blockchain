class Transaction(object):
	"""docstring for Transaction"""
	def __init__(self, sender, receiver, amount, time):
		super(Transaction, self).__init__()
		self.sender = sender
		self.receiver = receiver
		self.amount = amount
		self.time = time

	def __str__(self):
		return 'transaction: ' + self.sender + ' sending ' + str(self.amount) + ' to ' + self.receiver + ' at ' + str(self.time)
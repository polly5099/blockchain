from hashlib import sha256

class Transaction(object):
	"""docstring for Transaction"""
	def __init__(self, sender, receiver, amount, time):
		super(Transaction, self).__init__()
		self._sender = sender
		self._receiver = receiver
		self._amount = amount
		self._time = time
		self._consistent = False;
		self._hash = self.getHash();

	def getHash(self):
		if not self._consistent:
			self._hash = sha256(str(self).encode('utf-8')).hexdigest()
			self._consistent = True;
		return self._hash;

	def __str__(self):
		return 'transaction: ' + self._sender + ' sending ' + str(self._amount) + ' to ' + self._receiver + ' at ' + str(self._time)
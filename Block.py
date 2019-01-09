from Transaction import Transaction
import datetime
from hashlib import sha256
from encodings import aliases
import random

class Block(object):
    """docstring for ClassName"""
    id = None
    transaction = None
    currentDate = None
    previousBlock = None
    nextBlock = None
    nonce = None

    def __init__(self, previousBlock: 'Block', transaction: Transaction):
        super(Block, self).__init__()
        self.previousBlock = previousBlock
        self.transaction = transaction
        self.currentDate = datetime.datetime.now()

        #hasher = sha256()
        #previousBlockId = previousBlock.id if previousBlock is not None else ''
        #hasher.update(previousBlockId)
        #hashString = self.workBlock()
        self.id = self.workBlock() #sha256(hashString.encode('utf-8')).hexdigest()

    def workBlock(self):
        counter = 0;
        blockId = 'nope';

        while True:
            nonce = random.getrandbits(64)
            blockData = (self.previousBlock.id if self.previousBlock is not None else sha256(b'').hexdigest()) + str(self.transaction) + str(self.currentDate) + str(nonce);
            blockId = sha256(blockData.encode('utf-8')).hexdigest()
            ++counter

            if (counter > 100000 or blockId.startswith('0000')):
                break

        return blockId


    def printTracing(self):
        print(self)

        if (self.nextBlock != None):
            self.nextBlock.printTracing()

    def __str__(self):
        return 'blockId: ' + self.id + '\n' + str(self.transaction)
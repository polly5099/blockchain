from Transaction import Transaction
import datetime
from hashlib import sha256
from encodings import aliases
import random
from MerkleTools import MerkleTools

class Block(object):
    """docstring for ClassName"""
    id = None
    currentDate = None
    previousBlock = None
    nextBlock = None
    transactions = [];
    nonce = None

    def __init__(self, previousBlock: 'Block'):
        super(Block, self).__init__()
        self.previousBlock = previousBlock
        self.currentDate = datetime.datetime.now()
        self.merkleTree = MerkleTools();
        #hasher = sha256()
        #previousBlockId = previousBlock.id if previousBlock is not None else ''
        #hasher.update(previousBlockId)
        #hashString = self.workBlock()
        #self.id = self.workBlock() #sha256(hashString.encode('utf-8')).hexdigest()

    def mineBlock(self):
        counter = 0;
        rootHash = self.merkleTree.make_tree().get_merkle_root();

        while True:
            nonce = random.getrandbits(64)
            blockData = (self.previousBlock.id if self.previousBlock is not None else sha256(b'').hexdigest()) + rootHash + str(self.currentDate) + str(nonce);
            blockId = sha256(blockData.encode('utf-8')).hexdigest()
            ++counter

            if (blockId.startswith('0000')):
                self.id = blockId
                break

        return blockId

    def addTransaction(self, transaction: Transaction):
        self.transactions.append(transaction);
        self.merkleTree.add_leaf(transaction.getHash())


    def printTracing(self):
        print(self)

        if (self.nextBlock != None):
            self.nextBlock.printTracing()

    def __str__(self):
        return 'blockId: ' + self.id
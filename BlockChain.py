from Block import Block

class BlockChain(object):
    """docstring for BlockChain"""
    genesisBlock = None
    currentBlock = None
    blockCounter = 0

    def __init__(self):
        super(BlockChain, self).__init__()

    def addBlock(self, nextBlock:Block):
        if (self.genesisBlock == None):
            self.genesisBlock = nextBlock

        if (self.currentBlock is not None):
            self.currentBlock.nextBlock = nextBlock

        self.currentBlock = nextBlock
        self.currentBlock.id = self.blockCounter
        self.blockCounter += 1

    def printContent(self):
        return self.genesisBlock.printTracing()
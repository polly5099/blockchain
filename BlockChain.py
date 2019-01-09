from Block import Block

class BlockChain(object):
    """docstring for BlockChain"""
    genesisBlock = None
    currentBlock = None
    def __init__(self):
        super(BlockChain, self).__init__()


    def addBlock(self, nextBlock:Block):
        if (self.genesisBlock == None):
            self.genesisBlock = nextBlock

        self.currentBlock = nextBlock

    def printContent(self):
        return self.genesisBlock.printTracing()
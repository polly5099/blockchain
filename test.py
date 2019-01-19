from Block import Block
from Transaction import Transaction
from BlockChain import BlockChain
import datetime

transaction = Transaction('me', 'you', 100, datetime.datetime.now())

block = Block(None);
block.addTransaction(transaction);
block.mineBlock();
blockChain = BlockChain()
blockChain.addBlock(block)

print(blockChain.printContent())
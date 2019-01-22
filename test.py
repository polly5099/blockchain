from Block import Block
from Transaction import Transaction
from BlockChain import BlockChain
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

transaction = Transaction('me', 'you', 100, datetime.datetime.now())

with open('certificates/privatekey1.pem', 'rb') as keyFile:
    privateKey = serialization.load_pem_private_key(keyFile.read(), None, default_backend()) #default backend = openssl i think

blockChain = BlockChain()

block1 = Block(None);
block1.addTransaction(transaction);
block1.mineBlock(privateKey);
blockChain.addBlock(block1)

block2 = Block(block1.blockHash);
block2.addTransaction(transaction);
block2.mineBlock(privateKey);
blockChain.addBlock(block2)

block3 = Block(block2.blockHash);
block3.addTransaction(transaction);
block3.mineBlock(privateKey);
blockChain.addBlock(block3)

print(blockChain.printContent())
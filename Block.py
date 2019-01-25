from Transaction import Transaction
import datetime
from hashlib import sha256
from encodings import aliases
import random
from MerkleTools import MerkleTools
import hmac
import hashlib
import binascii
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

class Block(object):
    """docstring for ClassName"""
    id = None
    blockHash = None
    currentDate = None
    previousBlockHash = None
    nextBlock = None
    transactions = []
    nonce = None

    def __init__(self, previousBlockHash):
        super(Block, self).__init__()
        self.previousBlockHash = previousBlockHash
        self.currentDate = datetime.datetime.now()
        self.merkleTree = MerkleTools()
        #hasher = sha256()
        #previousBlockId = previousBlock.id if previousBlock is not None else ''
        #hasher.update(previousBlockId)
        #hashString = self.workBlock()
        #self.id = self.workBlock() #sha256(hashString.encode('utf-8')).hexdigest()

    def mine(self, privateKey):
        counter = 0;
        rootHash = self.merkleTree.make_tree().get_merkle_root();

        while True:
            nonce = random.getrandbits(64)
            serializedData = self.serializeData(rootHash, nonce);
            blockHash = self.signData(serializedData.encode('utf-8'), privateKey);
            #blockId = sha256(serializedData.encode('utf-8')).hexdigest()
            ++counter
            #print(str(blockHash))
            if (blockHash.startswith('000')):
                self.blockHash = blockHash
                print(blockHash)
                break

        return blockHash

    def serializeData(self, rootHash, nonce):
        return (self.previousBlockHash if self.previousBlockHash is not None else sha256(b'').hexdigest()) + rootHash + str(self.currentDate) + str(nonce);

    def signData(self, message, privateKey):
        #key = 'CCB45087D6527D1E478C33EE9D0C729DF677202C7E50114B58D4163BF42687F9'
        #with open('certificates/privatekey1.pem') as privKeyFile:
        #    key = privKeyFile.read()
        #byte_key = binascii.unhexlify(key)
        #message = message.encode()
        #return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()
        signature = privateKey.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        #print(signature)
        #print(type(signature))
        #print('flat decode', type(signature.hex()))
        #print('binascii', type(binascii.hexlify(signature)))
        #print(signature.decode('utf-8', 'ignore'))
        #publicKey = privateKey.public_key()
        #publicKey.verify(
        #    signature,
        #    message,
        #    padding.PSS(
        #        mgf=padding.MGF1(hashes.SHA256()),
        #        salt_length=padding.PSS.MAX_LENGTH
        #    ),
        #    hashes.SHA256()
        #)

        return signature.hex()

    def addTransaction(self, transaction: Transaction):
        self.transactions.append(transaction);
        self.merkleTree.add_leaf(transaction.getHash())


    def printTracing(self):
        print(self)

        if (self.nextBlock != None):
            self.nextBlock.printTracing()

    def __str__(self):
        return 'blockId: ' + str(self.id) + '\n' + 'blockHash: ' + self.blockHash
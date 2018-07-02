import hashlib as hasher
import datetime as date
import string
import itertools
import pytest

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(
            (str(self.index)+
            str(self.timestamp)+
            str(self.data)+
            str(self.previous_hash)).encode('utf-8')
        )
        return sha.hexdigest()

def create_genesis_block():
    return Block(0,date.datetime.now, 'this is first block data', '0')

def next_block(last_block):
    current_timestamp = date.datetime.now()
    current_index = last_block.index+1
    current_data = str(current_index)+string.ascii_lowercase

    current_hash = last_block.hash

    return Block(current_index, current_timestamp, current_data, current_hash)

number_of_blocks = 19



def create_blockchain():
    blockchain = [create_genesis_block()]
    for index in itertools.count():
        data = (yield)
        print('data: '+str(data))
        if data != 'chain':
            if data != 'q':
                myblock = Block(blockchain[index].index, date.datetime.now(), data, blockchain[index].hash)
                block = next_block(myblock)
            else:
                block = next_block(blockchain[index])
            blockchain.append(block)
            yield block.hash
        else:
            yield blockchain


if __name__ == "__main__":
    blockchain = create_blockchain()
    x = input()
    next(blockchain)
    res = 0
    while x != '':
        if x == 'q':
            res = blockchain.send(res)
        else:
            res = blockchain.send(x)
        next(blockchain)
        print(res)
        x = input()


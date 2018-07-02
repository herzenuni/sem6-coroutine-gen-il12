import blockchain
import pytest


class TestBlockchain:

    def test_size(self):
        b = blockchain.create_blockchain()
        next(b)
        b.send(1)
        next(b)
        b.send(2)
        next(b)
        b.send(3)
        next(b)
        res = b.send('chain')
        assert(len(res)==4)


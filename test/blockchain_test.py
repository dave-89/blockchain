import unittest
from datetime import datetime

from main.block import Block
from main.blockchain import BlockChain, first_proof


class BlockChainTest(unittest.TestCase):
    def test_creation(self):
        blockchain = BlockChain(address='my-address')
        chain = blockchain.chain
        self.assertEqual(len(chain), 1, 'wrong chain length at creation')
        self.assertEqual(len(chain[0].data['transactions']), 0, 'initial number of transactions different from 0')
        self.assertEqual(chain[0].data['pow'], first_proof, 'wrong first pow')
        self.assertEqual(chain[0].index, 0, 'wrong first index')

    def test_reward(self):
        blockchain = BlockChain(address='my-address')
        reward = blockchain.miner_reward()
        self.assertEqual(reward.frm, 'network', 'wrong reward - from')
        self.assertEqual(reward.to, 'my-address', 'wrong reward - to')
        self.assertEqual(reward.amount, 1, 'wrong reward - amount')


if __name__ == '__main__':
    unittest.main()

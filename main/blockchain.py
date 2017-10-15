from main.block import Block
from datetime import datetime
from time import time
import Crypto.PublicKey.RSA as RSA
import base64
from os import urandom as random

from main.exceptions.blockchain import PayerNotRegisteredException, InsufficientFundsException, \
    PayeeNotRegisteredException
from main.proof import do_proof
from main.state import State
from main.transaction import Transaction

first_proof = 'yrw6T6596icnddcUTWaxBF4UpiRcX0XF8224'


class BlockChain:
    def __init__(self, address):
        self.state = State()
        first_data = {'pow': first_proof, 'transactions': [], 'state': self.state}
        self.chain = [Block(0, datetime.now(), first_data, "0")]
        self.address = address
        self.keypair = RSA.generate(bits=1024, randfunc=random)

    def register_blockchain(self):
        self.state.add_user(self.address, self.keypair.publickey())

    def check_chain_through_consensus(self):
        # single node for now - consensus not implemented
        self.chain = self.chain

    @staticmethod
    def broadcast():
        # single node for now - no broadcast needed
        print('dummy broadcasting')

    def miner_reward(self):
        transaction = Transaction(frm='network', to=self.address, amount=1)
        encoded_transaction = base64.b64encode(transaction.dumps().encode('utf-8'))
        signature = self.keypair.sign(M=encoded_transaction, K=int(time()))
        transaction.signature = signature
        return transaction

    def update_state(self, transaction):
        users = self.state.users
        payer_id = transaction.frm
        payee_id = transaction.to
        if payer_id not in users:
            raise PayerNotRegisteredException('payer ' + payer_id + ' not registered')
        if payee_id not in users:
            raise PayeeNotRegisteredException('payee ' + payer_id + ' not registered')
        payer = users[payer_id]
        payee = users[payee_id]
        if not payer.validate_signature(transaction.dumps(), transaction.signature):
            raise InsufficientFundsException('invalid signature')
        if payer.amount < transaction.amount:
            raise InsufficientFundsException('not enough funds to cover the transaction')
        payer.balance -= transaction.amount
        payee.balance += transaction.amount

    @staticmethod
    def mine(last_pow):
        return do_proof(last_pow)

    def add_transaction(self, new_transactions):
        self.check_chain_through_consensus()
        last_block = self.chain[-1]
        last_pow = last_block.data['pow']
        new_pow = self.mine(last_pow)
        transactions = last_block.data['transactions'][:]
        for new_transaction in new_transactions:
            self.update_state(new_transaction)
            transactions.append(new_transaction)  # the new transaction
        transactions.append(self.miner_reward())  # reward for mining
        new_data = {'pow': new_pow, 'transactions': transactions}
        new_block = Block(index=last_block.index+1, ts=datetime.now(), data=new_data, previous_hash=last_block.hash)
        self.chain.append(new_block)
        self.broadcast()


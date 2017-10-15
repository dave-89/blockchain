import unittest
import base64

from main.transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_transaction_loads(self):
        transaction = Transaction(frm='me', to='you', amount=10)
        self.assertEqual(transaction.loads(), {"from": "me", "amount": 10, "to": "you"})

    def test_create_from_encoded(self):
        transaction = Transaction(signature='aaa')
        transaction.from_encoded(encoded=base64.b64encode('{"from": "me", "amount": 10, "to": "you"}'.encode('utf-8')))
        self.assertEqual(transaction.frm, 'me', msg='wrong from')
        self.assertEqual(transaction.to, 'you', msg='wrong to')
        self.assertEqual(transaction.amount, 10, msg='wrong amount')
        self.assertEqual(transaction.signature, 'aaa', msg='wrong signature')


if __name__ == '__main__':
    unittest.main()

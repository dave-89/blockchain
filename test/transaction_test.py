import unittest

from main.transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_transaction_loads(self):
        transaction = Transaction(frm='me', to='you', amount=10)
        self.assertEqual(transaction.loads(), {"from": "me", "amount": 10, "to": "you"})

    def test_transaction_dumps(self):
        transaction = Transaction(frm='me', to='you', amount=10)
        self.assertEqual(transaction.dumps(), '{"to": "you", "amount": 10, "from": "me"}')


if __name__ == '__main__':
    unittest.main()

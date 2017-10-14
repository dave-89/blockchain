import json


class Transaction:
    def __init__(self, frm, to, amount, signature):
        self.frm = frm
        self.to = to
        self.amount = amount
        self.signature = signature

    def dumps(self):
        return json.dumps(self.loads())

    def loads(self):
        return {'from': self.frm, 'to': self.to, 'amount': self.amount}

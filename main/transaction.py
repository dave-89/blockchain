import json
import base64


class Transaction:
    def __init__(self, frm=None, to=None, amount=None, signature=None):
        self.frm = frm
        self.to = to
        self.amount = amount
        self.signature = signature

    def from_encoded(self, encoded):
        data = json.loads(base64.b64decode(encoded).decode('utf-8'))
        self.frm = data['from']
        self.to = data['to']
        self.amount = data['amount']

    def dumps(self):
        return json.dumps(self.loads())

    def loads(self):
        return {'from': self.frm, 'to': self.to, 'amount': self.amount}

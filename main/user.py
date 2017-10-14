class User:
    def __init__(self, pub_key):
        self.pub_key = pub_key
        self.balance = 0

    def validate_signature(self, plain_data, signed_data):
        return True
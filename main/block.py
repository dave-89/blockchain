import hashlib


class Block:
    def __init__(self, index, ts, data, previous_hash):
        self.index = index
        self.ts = ts
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return str(self.index) + str(self.ts) + str(self.data) + str(self.previous_hash)

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self).encode('utf-8'))
        return sha.hexdigest()

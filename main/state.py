from main.user import User


class State:
    def __init__(self):
        self.users = {}

    def add_user(self, user, pub_key):
        self.users[user] = User(pub_key=pub_key)
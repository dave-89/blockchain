class PayerNotRegisteredException(Exception):
    def __init__(self, reason):
        self.reason = reason


class PayeeNotRegisteredException(Exception):
    def __init__(self, reason):
        self.reason = reason


class PayerNotAuthorisedException(Exception):
    def __init__(self, reason):
        self.reason = reason


class InsufficientFundsException(Exception):
    def __init__(self, reason):
        self.reason = reason
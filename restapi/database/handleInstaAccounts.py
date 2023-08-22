from .connection import Database

class Accounts(Database):
    def __init__(self):
        super().__init__()
        self.accounts = self.db.instagramaccounts
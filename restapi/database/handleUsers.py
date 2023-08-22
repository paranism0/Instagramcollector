from .connection import Database

class Users(Database):
    def __init__(self):
        super().__init__()
        self.users = self.db.users
        self.users2 = self.nonasyncdb.users
    def initialCollections(self):
        self.users2.create_index("username" , unique = True)
        self.users2.create_index("email" , unique = True)
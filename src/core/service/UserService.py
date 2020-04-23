from src.core.base.Service import Service
from src.core.db.UserRepository import UserDao


class UserService(Service):
    def __init__(self):
        self.dao = UserDao()

    def save(self, data):
        pass

    def update(self, data):
        pass

    def list(self):
        pass


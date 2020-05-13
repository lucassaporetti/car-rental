from abc import abstractmethod
from src.core.base.interfaces.repository import Repository


class DbRepository(Repository):
    def __init__(self, filename):
        super().__init__(filename)

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def count(self):
        pass

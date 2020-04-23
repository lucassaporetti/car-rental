from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def find_all(self, data):
        pass

    @abstractmethod
    def find_by_id(self, data):
        pass

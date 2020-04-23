from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def list(self):
        pass

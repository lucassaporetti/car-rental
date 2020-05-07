from abc import ABC, abstractmethod

from src.model.entity import Entity


class Repository(ABC):
    @abstractmethod
    def __init__(self, filename):
        pass

    @abstractmethod
    def insert(self, entity: Entity):
        pass

    @abstractmethod
    def update(self, entity: Entity):
        pass

    @abstractmethod
    def delete(self, entity: Entity):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, entity_id: str):
        pass

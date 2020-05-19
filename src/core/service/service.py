from abc import ABC

from src.core.repository.repository import Repository
from src.model.entity import Entity


class Service(ABC):
    def __init__(self, repository: Repository):
        self.repository = repository

    def save(self, entity: Entity):
        if entity.uuid is None or self.repository.find_by_id(entity.uuid) is None:
            self.repository.insert(entity)
        else:
            self.repository.update(entity)

    def remove(self, entity: Entity):
        self.repository.delete(entity)

    def list(self, filters: str = None) -> list:
        return self.repository.find_all(filters=filters)

    def get(self, uuid: str) -> Entity:
        return self.repository.find_by_id(uuid)

from abc import ABC

from src.core.base.Repository import Repository
from src.model.Entity import Entity


class Service(ABC):
    def __init__(self, dao: Repository):
        self.dao = dao

    def save(self, data: Entity):
        existing = self.dao.find_by_id(data.uuid)
        if existing is None:
            self.dao.insert(data)
        else:
            self.dao.update(data)

    def list(self):
        return self.dao.find_all()

    def get(self, uuid: str):
        return self.dao.find_by_id(uuid)

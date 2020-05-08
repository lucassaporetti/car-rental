from src.core.base.interfaces.repository import Repository
from src.model.entity import Entity


class DbRepository(Repository):
    def __init__(self, filename):
        super().__init__(filename)

    def insert(self, entity: Entity):
        pass

    def update(self, entity: Entity):
        pass

    def delete(self, entity: Entity):
        pass

    def find_all(self):
        pass

    def find_by_id(self, entity_id: str):
        pass


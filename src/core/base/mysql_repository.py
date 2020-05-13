from src.core.base.interfaces.db_repository import DbRepository
from src.model.entity import Entity


class MySqlRepository(DbRepository):
    def __init__(self, filename):
        super().__init__(filename)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def is_connected(self):
        pass

    def count(self):
        pass

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

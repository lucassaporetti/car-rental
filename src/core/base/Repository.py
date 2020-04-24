from abc import ABC

from src.core.base.local_db import LocalDB
from src.model.entity import Entity


class Repository(ABC):
    def __init__(self, filename):
        self.db_filename = filename
        self.localDb = LocalDB(self.db_filename)

    def insert(self, entity: Entity):
        self.localDb.data.append(entity.__dict__)
        self.localDb.commit()
        print("{} has been saved !".format(entity.__class__.__name__))

    def update(self, entity: Entity):
        idx = self.localDb.data.index(entity)
        self.localDb.data[idx] = entity
        self.localDb.commit()
        print("{} has been updated !".format(entity.__class__.__name__))

    def delete(self, entity: Entity):
        idx = self.localDb.data.index(entity)
        self.localDb.data.remove(self.localDb.data[idx])
        self.localDb.commit()
        print("{} has been deleted !".format(entity.__class__.__name__))

    def find_all(self):
        return self.localDb.data

    def find_by_id(self, uuid: str):
        return None

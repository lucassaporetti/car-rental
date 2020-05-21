import re
import uuid

from typing import Optional

from src.core.repositories.file.file_db import LocalDB
from src.core.repositories.repository import Repository
from src.core.tools.commons import check_criteria
from core.models.entity import Entity


class FileRepository(Repository):
    def __init__(self, filename):
        super().__init__(filename)
        self.db_filename = filename
        self.localDb = LocalDB(self.db_filename)

    def insert(self, entity: Entity):
        entity.uuid = entity.uuid if entity.uuid is not None else uuid.uuid4()
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

    def find_all(self, filters: str = None) -> Optional[list]:
        if filters is not None:
            file_filters = filters.split(',')
            filtered = []
            for next_filter in file_filters:
                fields = re.split('=|>|<|>=|<=|==|!=', next_filter)
                found = [c for c in self.localDb.data if check_criteria(fields[1], c[fields[0]])]
                filtered.extend(found)
            return filtered
        else:
            return self.localDb.data

    def find_by_id(self, entity_id: str) -> Optional[Entity]:
        if entity_id:
            result = [c for c in self.localDb.data if entity_id == c['uuid']]
            return result if len(result) > 0 else None
        else:
            return None

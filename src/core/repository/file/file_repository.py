import re
import uuid
from abc import abstractmethod
from typing import Optional

from core.config.app_configs import AppConfigs
from core.model.entity import Entity
from src.core.repository.file.file_storage import FileStorage
from src.core.repository.repository import Repository
from src.core.tools.commons import check_criteria, log_init


class FileRepository(Repository):

    __storages = {}

    def __init__(self, filename: str):
        super().__init__(filename)
        self.log = log_init(AppConfigs.log_file())
        self.db_filename = filename
        self.localDb = self.__create_or_get()

    def __create_or_get(self):
        if self.db_filename in FileRepository.__storages:
            return FileRepository.__storages[self.db_filename]
        else:
            FileRepository.__storages[self.db_filename] = FileStorage(self.db_filename)
            return FileRepository.__storages[self.db_filename]

    def insert(self, entity: Entity):
        entity.uuid = entity.uuid if entity.uuid is not None else uuid.uuid4()
        self.localDb.data.append(entity.__dict__)
        self.localDb.commit()
        self.log.info("{} has been saved !".format(entity.__class__.__name__))

    def update(self, entity: Entity):
        idx = self.localDb.data.index(entity)
        self.localDb.data[idx] = entity
        self.localDb.commit()
        self.log.info("{} has been updated !".format(entity.__class__.__name__))

    def delete(self, entity: Entity):
        idx = self.localDb.data.index(entity)
        self.localDb.data.remove(self.localDb.data[idx])
        self.localDb.commit()
        self.log.info("{} has been deleted !".format(entity.__class__.__name__))

    def find_all(self, filters: str = None) -> Optional[list]:
        if filters is not None:
            file_filters = filters.split(',')
            filtered = []
            for next_filter in file_filters:
                fields = re.split('=|>|<|>=|<=|==|!=', next_filter)
                try:
                    found = [self.row_to_entity(c) for c in self.localDb.data if
                             check_criteria(fields[1], c[fields[0]])]
                except KeyError:
                    continue
                filtered.extend(found)
            return filtered
        else:
            return [self.row_to_entity(c) for c in self.localDb.data]

    def find_by_id(self, entity_id: str) -> Optional[Entity]:
        if entity_id:
            result = [c for c in self.localDb.data if entity_id == c['uuid']]
            return result if len(result) > 0 else None
        else:
            return None

    @abstractmethod
    def row_to_entity(self, row: tuple) -> Entity:
        pass

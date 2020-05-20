from abc import abstractmethod

from src.configs import AppConfigs
from src.core.factory.sql_factory import SqlFactory
from src.core.repository.repository import Repository


class DbRepository(Repository):
    def __init__(self, sql_factory: SqlFactory):
        super().__init__(sql_factory.sql_template_file)
        self.sql_factory = sql_factory
        if 'DATABASE' == AppConfigs\
                .app_properties.get('persistence.repository.type').upper():
            self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def count(self):
        pass

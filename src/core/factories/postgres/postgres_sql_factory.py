from src.core.factories.sql_factory import SqlFactory


class PostgresFactory(SqlFactory):
    def __init__(self, sql_template_file: str):
        super().__init__(sql_template_file)

    def count(self):
        pass

    def insert(self, values: dict):
        pass

    def update(self,  values: dict = None, filters: list = None):
        pass

    def delete(self, filters: list = None):
        pass

    def select(self, columns: list = None, filters: list = None):
        pass

from src.core.properties import Properties
from src.model.entity import Entity


class SqlFactory:
    @staticmethod
    def dict_to_values(values: dict) -> str:
        str_values = ''
        for key, value in values.items():
            str_values += "{}'{}'".format(value, ', ' if str_values else '')
        return str_values

    def __init__(self, sql_template_file):
        self.sql_templates = Properties(sql_template_file)
        self.sql_templates.read()

    def count(self, table_name: str):
        return self.sql_templates\
            .get('count')\
            .replace('{TABLE_NAME}', table_name.upper())

    def insert(self, table_name: str, values: dict):
        return self.sql_templates\
            .get('insert') \
            .replace('{TABLE_NAME}', table_name.upper()) \
            .replace('{INSERT_VALUES}', SqlFactory.dict_to_values(values))


class CarFactory(SqlFactory):
    def __init__(self, sql_template_file):
        super().__init__(sql_template_file)



from abc import abstractmethod

from src.core.properties import Properties


class SqlFactory:
    @staticmethod
    def dict_to_values(values: dict) -> str:
        str_values = ''
        for key, value in values.items():
            if value is not None:
                sep = ', ' if str_values else ''
                str_values += "{}'{}'".format(sep, value)

        return str_values

    @staticmethod
    def list_to_filters(filters: list) -> str:
        str_filters = ''
        for sql_filter in filters:
            sep = ', ' if str_filters else ''
            str_filters += "{}AND {}".format(sep, sql_filter)

        return str_filters

    @staticmethod
    def list_to_columns(columns: list) -> str:
        str_columns = ''
        for key, value in columns:
            if value is not None:
                sep = ', ' if str_columns else ''
                str_columns += "{}{}".format(sep, key.upper(), value)

        return str_columns

    def __init__(self, sql_template_file: str):
        self.sql_template_file = sql_template_file
        self.sql_templates = Properties(sql_template_file)
        self.sql_templates.read()

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def insert(self, values: dict):
        pass

    @abstractmethod
    def update(self,  values: dict = None, filters: list = None):
        pass

    @abstractmethod
    def delete(self, filters: list = None):
        pass

    @abstractmethod
    def select(self, columns: list = None, filters: list = None):
        pass

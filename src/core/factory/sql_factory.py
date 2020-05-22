from abc import abstractmethod, ABC

from src.core.tools.properties import Properties


class SqlFactory(ABC):
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

    @staticmethod
    def dict_to_field_set(values: dict) -> str:
        str_field_set = ''
        for key, value in values.items():
            if value is not None:
                sep = ', ' if str_field_set else ''
                str_field_set += "{}{} = '{}'".format(sep, key.upper(), value)

        return str_field_set

    def __init__(self, sql_template_file: str):
        self.sql_template_file = sql_template_file
        self.sql_templates = Properties(sql_template_file)

    def __str__(self):
        return self.__class__.__name__

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

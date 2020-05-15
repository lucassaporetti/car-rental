
from src.core.properties import Properties
from src.core.tools import dict_to_values, list_to_filters, list_to_columns


class SqlFactory:
    def __init__(self, sql_template_file):
        self.sql_template_file = sql_template_file
        self.sql_templates = Properties(sql_template_file)
        self.sql_templates.read()

    def count(self):
        return self.sql_templates.get('count')

    def insert(self, values: dict):
        return self.sql_templates.get('insert').format(dict_to_values(values))

    def update(self,  values: dict = None, filters: dict = None):
        return self.sql_templates.get('update')\
            .format(
                dict_to_values(values) if values is not None else '',
                list_to_filters(filters) if filters is not None else '',
            )

    def delete(self, filters: dict = None):
        return self.sql_templates.get('delete')\
            .format(
                list_to_filters(filters) if filters is not None else '',
            )

    def select(self, columns: list = None, filters: list = None):
        return self.sql_templates.get('select')\
            .format(
                list_to_columns(columns) if columns is not None else '*',
                list_to_filters(filters) if filters is not None else '',
            )


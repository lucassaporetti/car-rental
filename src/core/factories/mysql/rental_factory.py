
from core.config.app_configs import AppConfigs
from src.core.factories.mysql.mysql_factory import MySqlFactory


class RentalFactory(MySqlFactory):

    sql_template_file = "sql/mysql/ddl/rental_templates.properties"

    def __init__(self):
        super().__init__(RentalFactory.sql_template_file)

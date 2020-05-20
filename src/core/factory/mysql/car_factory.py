
from src.configs import AppConfigs
from src.core.factory.mysql.mysql_factory import MySqlFactory


class CarFactory(MySqlFactory):

    sql_template_file = f"{AppConfigs.cur_dir}/sql/mysql/ddl/car_templates.properties"

    def __init__(self):
        super().__init__(CarFactory.sql_template_file)

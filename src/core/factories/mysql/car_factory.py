
from src.app_configs import AppConfigs
from src.core.factories.mysql.mysql_factory import MySqlFactory


class CarFactory(MySqlFactory):

    sql_template_file = "{}/sql/mysql/ddl/car_templates.properties".format(AppConfigs.root_dir())

    def __init__(self):
        super().__init__(CarFactory.sql_template_file)

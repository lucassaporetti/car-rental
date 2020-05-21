
from core.config.app_configs import AppConfigs
from src.core.factories.mysql.mysql_factory import MySqlFactory


class CustomerFactory(MySqlFactory):

    sql_template_file = f"{AppConfigs.root_dir()}/sql/mysql/ddl/customer_templates.properties"

    def __init__(self):
        super().__init__(CustomerFactory.sql_template_file)

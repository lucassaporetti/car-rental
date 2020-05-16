
from src.main import Main
from src.core.factory.mysql.mysql_factory import MySqlFactory


class CustomerFactory(MySqlFactory):

    sql_template_file = f"{Main.cur_dir}/sql/mysql/ddl/customer_templates.properties"

    def __init__(self):
        super().__init__(CustomerFactory.sql_template_file)

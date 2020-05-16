
from src.main import Main
from src.core.factory.mysql.mysql_factory import MySqlFactory


class EmployeeFactory(MySqlFactory):

    sql_template_file = f"{Main.cur_dir}/sql/mysql/ddl/employee_templates.properties"

    def __init__(self):
        super().__init__(EmployeeFactory.sql_template_file)
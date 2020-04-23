from src.core.base.Menu import Menu

MENU = """\033[2J
[A] Employee
[B] Customer
[C] Previous Menu
"""


class UserUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C']

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            print('Add Employee')
        elif str_op == 'B':
            print('Add Customer')
        elif str_op == 'C':
            print('Previous Menu')
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options


from src.core.base.Menu import Menu
from src.ui.ListingUi import ListingUi
from src.ui.UserUi import UserUi

MENU = """\033[2J
[0] Exit
[1] Add Car Model
[2] Add User
[3] Rent a Car
[4] Return a Car
[5] Car Information
[6] Listing
"""


class MainMenuUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = range(0, 7)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return Menu.EXIT_REQUEST
        elif int_op == 1:
            print('Add Car Model')
        elif int_op == 2:
            print('Add User')
            return UserUi()
        elif int_op == 3:
            print('Rent a Car')
        elif int_op == 4:
            print('Return a Car')
        elif int_op == 5:
            print('Car Information')
        elif int_op == 6:
            print('Listing')
            return ListingUi()

        return Menu.SAME_MENU

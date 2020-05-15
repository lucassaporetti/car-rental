from time import sleep


def is_integer(number):
    return str(number).isdigit()


def is_float(number):
    return str(number).isdecimal()


def print_error(msg: str, arg: str = None):
    print(f"\033[0;31m### Error: {msg} \"{arg}\"\033[0;0;0m")
    sleep(2.5)
    print('\033[2A\033[J', end='')


def print_warning(msg: str, arg: str = None):
    print(f"\033[0;93m### Warn: {msg} \"{arg}\"\033[0;0;0m")
    sleep(2.5)
    print('\033[2A\033[J', end='')


def print_list(the_list: list):
    print('\033[2J\033[H')
    print('-='*80)
    for next_item in the_list:
        if the_list.index(next_item) > 0:
            print('-+'*80)
        print('\033[0;36m{}\033[0;0;0m'.format(next_item))
    print('-='*80)
    print('')
    press_enter()


def print_one(entity):
    print_list(entity)
    press_enter()


def press_enter():
    print('')
    input('Press \033[0;32m[Enter]\033[0;0;0m to continue ...')


def check_criteria(partial_value, whole_value):
    if isinstance(whole_value, str):
        return str(partial_value).upper() in whole_value.upper()
    elif isinstance(whole_value, int):
        return int(partial_value) == whole_value
    else:
        return False


def dict_to_values(values: dict) -> str:
    str_values = ''
    for key, value in values.items():
        if value is not None:
            sep = ', ' if str_values else ''
            str_values += "{}'{}'".format(sep, value)

    return str_values


def list_to_filters(filters: list) -> str:
    str_filters = ''
    for sql_filter in filters:
        sep = ', ' if str_filters else ''
        str_filters += "{}AND {}".format(sep, sql_filter)

    return str_filters


def list_to_columns(columns: list) -> str:
    str_columns = ''
    for key, value in columns:
        if value is not None:
            sep = ', ' if str_columns else ''
            str_columns += "{}{}".format(sep, key.upper(), value)

    return str_columns

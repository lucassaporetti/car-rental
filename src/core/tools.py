from time import sleep


def is_integer(number):
    return str(number).isdigit()


def is_float(number):
    return str(number).isdecimal()


def print_error(msg: str, arg: str):
    print(f"### Error: {msg} \"{arg}\"")
    sleep(1)
    print('\033[2A\033[J', end='')


def dict_to_values(values: dict) -> str:
    str_values = ''
    for key, value in values.items():
        if value is not None:
            sep = ', ' if str_values else ''
            str_values += "{}'{}'".format(sep, value)
    return str_values


def dict_to_filters(values: dict) -> str:
    return ''


from time import sleep


def is_integer(number):
    return str(number).isdigit()


def is_float(number):
    return str(number).isdecimal()


def print_error(msg: str, arg: str):
    print(f"### Error: {msg} \"{arg}\"")
    sleep(1)
    print('\033[2A\033[J', end='')


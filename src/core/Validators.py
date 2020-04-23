import re
from datetime import datetime
from typing import Type


class Validators:
    @staticmethod
    def validate_string(string: str, pattern: str, min_len: int = 0, max_len: int = 30):
        str_len = len(string)
        return min_len < str_len <= max_len and bool(re.match(pattern, string))

    @staticmethod
    def validate_int(number: int, min_value: int = 0, max_value: int = 1000000):
        return min_value < number <= max_value

    @staticmethod
    def validate_float(number: float, min_value: float = 0, max_value: float = 1000000):
        return min_value < number <= max_value

    @staticmethod
    def validate_enum(name: str, enum_type: Type):
        return name.upper() in enum_type.__dict__

    @staticmethod
    def validate_date(date_text: str, fmt: str):
        try:
            datetime.strptime(date_text, fmt)
            return True
        except ValueError:
            return False


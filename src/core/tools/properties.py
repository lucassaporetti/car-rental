from typing import Optional


class Properties:
    def __init__(self, filename):
        self.filename = filename
        self.properties = {}

    def get(self, key: str) -> str:
        return self.properties[key.strip().upper()] if key.strip().upper() in self.properties else None

    def get_int(self, key: str) -> Optional[int]:
        try:
            return int(self.get(key))
        except TypeError:
            return None

    def get_float(self, key: str) -> Optional[float]:
        try:
            return float(self.get(key))
        except TypeError:
            return None

    def get_bool(self, key: str) -> Optional[bool]:
        try:
            return bool(self.get(key))
        except TypeError:
            return None

    def read(self):
        with open(self.filename, 'r') as f_properties:
            all_properties = f_properties.readlines()
            for prop in all_properties:
                if prop.startswith('#'):
                    continue
                parts = prop.split('=', 1)
                if len(parts) != 2:
                    continue
                key = parts[0].strip().upper()
                value = parts[1].strip()
                self.properties[key] = value

        return self

    def size(self) -> int:
        return len(self.properties)

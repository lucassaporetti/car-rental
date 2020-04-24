import ast
import os


class LocalDB:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = []
        self.load()

    def load(self):
        mode = 'r+' if os.path.exists(self.filename) else 'w+'
        with open(self.filename, mode) as f_local_db:
            lines = f_local_db.read()
            if lines:
                saved_data = ast.literal_eval(lines)
                self.data = saved_data

    def commit(self):
        with open(self.filename, 'w') as f_local_db:
            f_local_db.write(str(self.data))

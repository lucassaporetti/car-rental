import ast
import os

from core.config.app_configs import AppConfigs
from core.tools.commons import log_init


class FileStorage:
    def __init__(self, filename: str):
        self.log = log_init(AppConfigs.log_file())
        self.filename = filename
        self.data = []
        self.load()
        self.log.info('File storage created filename={} entries={}'.format(filename, len(self.data)))

    def load(self):
        mode = 'r+' if os.path.exists(self.filename) else 'w+'
        with open(self.filename, mode) as f_local_db:
            lines = f_local_db.read()
            if lines:
                saved_data = ast.literal_eval(lines)
                self.data = saved_data

    def commit(self):
        with open(self.filename, 'w') as f_local_db:
            data = str(self.data)
            f_local_db.write(data)

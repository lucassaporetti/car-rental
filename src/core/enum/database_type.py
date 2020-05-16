from enum import Enum


class DatabaseType(Enum):
    MYSQL = 'Mysql Database'
    POSTGRES = 'Postgres Database'
    ARCHIVE = 'Local File Database'

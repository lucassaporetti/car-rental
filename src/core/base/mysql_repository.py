import pathlib
import sys
import uuid

from src.core.base.interfaces.db_repository import DbRepository
from src.core.factories import SqlFactory
from src.core.properties import Properties
from src.model.entity import Entity
import pymysql

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
DB_PROPERTIES = Properties(f"{CUR_DIR}/db.properties").read()


class MySqlRepository(DbRepository):
    def __init__(self, sql_factory: SqlFactory):
        super().__init__(sql_factory)
        self.hostname = DB_PROPERTIES.get('db.hostname')
        self.port = DB_PROPERTIES.get_int('db.port')
        self.user = DB_PROPERTIES.get('db.user')
        self.password = DB_PROPERTIES.get('db.password')
        self.database = DB_PROPERTIES.get('db.database')
        self.connector = None
        self.cursor = None
        self.connect()

    def is_connected(self):
        return self.connector is not None

    def connect(self):
        if not self.is_connected():
            self.connector = pymysql.connect(
                host=self.hostname,
                user=self.user,
                port=self.port,
                password=self.password,
                database=self.database
            )
            assert self.is_connected(), 'ERROR: Unable to connect with {}@{}:{}/{}'\
                .format(self.user, self.hostname, self.port, self.database)
            self.cursor = self.connector.cursor()
            print('Connection with {}@{}:{}/{} established.'.format(self.user, self.hostname, self.port, self.database))
        return self.connector

    def disconnect(self):
        if self.is_connected():
            self.connector.close()
            print('Disconnected from {}@{}:{}/{}.'.format(self.user, self.hostname, self.port, self.database))
            self.connector = None
        else:
            print('ERROR: Connection with {}@{}:{}/{} was not established.'.format(self.user, self.hostname, self.port, self.database))
        return self.connector

    def count(self):
        pass

    def insert(self, entity: Entity):
        entity.uuid = entity.uuid if entity.uuid is not None else uuid.uuid4()
        insert_stm = self.sql_factory.insert(entity.__dict__)
        print('Executing SQL statement: {}'.format(insert_stm))
        self.cursor.execute(insert_stm)
        self.connector.commit()

    def update(self, entity: Entity):
        pass

    def delete(self, entity: Entity):
        pass

    def find_all(self):
        select_stm = self.sql_factory.select()
        print('Executing SQL statement: {}'.format(select_stm))
        self.cursor.execute(select_stm)
        result = self.cursor.fetchall()
        ret_val = []
        for next_row in result:
            ret_val.append(next_row)

        return ret_val

    def find_by_id(self, entity_id: str):
        pass

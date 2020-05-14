from src.core.base.interfaces.db_repository import DbRepository
from src.model.entity import Entity
import pymysql


class MySqlRepository(DbRepository):
    def __init__(self, filename, user, password, hostname, port, database, table_name):
        super().__init__(filename)
        self.db_name = filename
        self.user = user
        self.password = password
        self.hostname = hostname
        self.port = port
        self.database = database
        self.table_name = table_name
        self.connector = None

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
            assert self.is_connected(), 'ERROR: Unable to connect with {}@{}:{}/{}'.format(self.user, self.hostname,
                                                                                           self.port, self.database)
            print('Connection with {}@{}:{}/{} established.'.format(self.user, self.hostname,
                                                                    self.port, self.database))
        return self.connector

    def disconnect(self):
        if self.is_connected():
            self.connector.close()
            print('Disconnected from {}@{}:{}/{}.'.format(self.user, self.hostname,
                                                          self.port, self.database))
            self.connector = None
        else:
            print('ERROR: Connection with {}@{}:{}/{} was not established.'.format(self.user, self.hostname,
                                                                                   self.port, self.database))
        return self.connector

    def count(self):
        if self.is_connected():
            my_cursor = self.connector.cursor()
            my_cursor.execute("SELECT COUNT(UUID) FROM {}".format(self.table_name))
            my_result = my_cursor.fetchall()
            for x in my_result:
                print(x)
        else:
            print('ERROR: Connection with {}@{}:{}/{} was not established.'.format(self.user, self.hostname,
                                                                                   self.port, self.database))

    def insert(self, entity: Entity):
        pass

    def update(self, entity: Entity):
        pass

    def delete(self, entity: Entity):
        pass

    def find_all(self):
        pass

    def find_by_id(self, entity_id: str):
        pass


cars = None
ob = MySqlRepository(cars, 'root', '123G@biroba4', 'localhost', 3306, 'car_rental_db', 'CARS')
ob.connect()
ob.is_connected()
ob.count()
ob.disconnect()
ob.count()

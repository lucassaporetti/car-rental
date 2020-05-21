import pathlib
import sys
from abc import ABC
from datetime import datetime

from src.core.enums.database_type import DatabaseType
from src.core.enums.repository_type import RepositoryType
from src.core.tools.commons import log_init
from src.core.tools.properties import Properties


class AppConfigs(ABC):
    root_dir = pathlib.Path(sys.argv[0]).parent.absolute()
    log_file = "{}/../log/car-rental.log".format(root_dir)
    log = log_init(log_file)
    app_properties = Properties("{}/resources/application.properties".format(
        root_dir)).read()
    log.debug('Successfully read {} properties'.format(app_properties.size()))
    repository_type = RepositoryType[app_properties.get(
        'persistence.repository.type').upper()]
    database_type = DatabaseType[app_properties.get(
        'persistence.database.type').upper()]
    log.info('Car Rental started {} using repository_type={} and database_type={}'.format(
        datetime.now(), repository_type, database_type))

    @staticmethod
    def get_prop(property_name: str):
        return AppConfigs.app_properties.get(property_name)

    @staticmethod
    def get_root_dir():
        return AppConfigs.root_dir

    @staticmethod
    def get_repository_typ():
        return AppConfigs.repository_type

    @staticmethod
    def get_database_type():
        return AppConfigs.database_type

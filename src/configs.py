import pathlib
import sys
from datetime import datetime

from src.core.enums.database_type import DatabaseType
from src.core.enums.repository_type import RepositoryType
from src.core.tools.commons import log_init
from src.core.tools.properties import Properties


class AppConfigs:
    cur_dir = pathlib.Path(sys.argv[0]).parent.absolute()
    log_file = f"{cur_dir}/../log/car-rental.log"
    log = log_init(log_file)
    log.info('Car Rental started {}'.format(datetime.now()))
    app_properties = Properties(f"{cur_dir}/resources/application.properties").read()
    log.info('Successfully read {} properties'.format(app_properties.size()))
    repository_type = RepositoryType[app_properties.get('persistence.repository.type').upper()]
    database_type = DatabaseType[app_properties.get('persistence.database.type').upper()]

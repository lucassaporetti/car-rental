from abc import ABC
from typing import Optional, Type

from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.repository.db.mysql.car_repository import CarRepository as MysqlCarRepository
from src.core.repository.db.mysql.customer_repository import CustomerRepository as MysqlCustomerRepository
from src.core.repository.db.mysql.employee_repository import EmployeeRepository as MysqlEmployeeRepository
from src.core.repository.db.mysql.rental_repository import RentalRepository as MysqlRentalRepository
from src.core.repository.file.car_repository import CarRepository as FileCarRepository
from src.core.repository.file.customer_repository import CustomerRepository as FileCustomerRepository
from src.core.repository.file.employee_repository import EmployeeRepository as FileEmployeeRepository
from src.core.repository.file.rental_repository import RentalRepository as FileRentalRepository
from src.core.repository.repository import Repository
from src.core.tools.commons import log_init

LOG = log_init(AppConfigs.log_file())


class RepositoryFacade(ABC):
    __cache = {}
    __repositories = {
        RepositoryType.FILE: {
            DatabaseType.ARCHIVE: {
                Model.CAR: FileCarRepository,
                Model.CUSTOMER: FileCustomerRepository,
                Model.EMPLOYEE: FileEmployeeRepository,
                Model.RENTAL: FileRentalRepository,
            }
        },
        RepositoryType.DATABASE: {
            DatabaseType.MYSQL: {
                Model.CAR: MysqlCarRepository,
                Model.CUSTOMER: MysqlCustomerRepository,
                Model.EMPLOYEE: MysqlEmployeeRepository,
                Model.RENTAL: MysqlRentalRepository,
            },
            DatabaseType.POSTGRES: {
                Model.CAR: None,
                Model.CUSTOMER: None,
                Model.EMPLOYEE: None,
                Model.RENTAL: None,
            }
        }
    }

    @staticmethod
    def create_or_get(repository_class: Type):
        cache_key = repository_class.__name__
        if cache_key in RepositoryFacade.__cache:
            LOG.info('Retrieving repository {}'.format(cache_key))
            return RepositoryFacade.__cache[cache_key]
        else:
            LOG.info('Creating repository {}'.format(cache_key))
            RepositoryFacade.__cache[cache_key] = repository_class()
            return RepositoryFacade.__cache[cache_key]

    @staticmethod
    def get(repository_type: RepositoryType, database_type: DatabaseType, model: Model) -> Optional[Repository]:
        repository_class = RepositoryFacade.__repositories[repository_type][database_type][model]
        repository = RepositoryFacade.create_or_get(repository_class)
        return repository

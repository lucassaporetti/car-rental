from abc import ABC
from typing import Optional
from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.repository.repository import Repository
from src.core.tools.commons import log_init

from src.core.repository.file.car_repository import CarRepository as FileCarRepository
from src.core.repository.file.customer_repository import CustomerRepository as FileCustomerRepository
from src.core.repository.file.employee_repository import EmployeeRepository as FileEmployeeRepository
from src.core.repository.file.rental_repository import RentalRepository as FileRentalRepository

from src.core.repository.db.mysql.car_repository import CarRepository as MysqlCarRepository
from src.core.repository.db.mysql.customer_repository import CustomerRepository as MysqlCustomerRepository
from src.core.repository.db.mysql.employee_repository import EmployeeRepository as MysqlEmployeeRepository
from src.core.repository.db.mysql.rental_repository import RentalRepository as MysqlRentalRepository

LOG = log_init(AppConfigs.log_file())


class RepositoryFacade(ABC):

    __repositories = {
        RepositoryType.FILE.name: {
            DatabaseType.ARCHIVE.name: {
                Model.CAR.name: FileCarRepository,
                Model.CUSTOMER.name: FileCustomerRepository,
                Model.EMPLOYEE.name: FileEmployeeRepository,
                Model.RENTAL.name: FileRentalRepository,
            }
        },
        RepositoryType.DATABASE.name: {
            DatabaseType.MYSQL.name: {
                Model.CAR.name: MysqlCarRepository,
                Model.CUSTOMER.name: MysqlCustomerRepository,
                Model.EMPLOYEE.name: MysqlEmployeeRepository,
                Model.RENTAL.name: MysqlRentalRepository,
            },
            DatabaseType.POSTGRES.name: {
                Model.CAR.name: None,
                Model.CUSTOMER.name: None,
                Model.EMPLOYEE.name: None,
                Model.RENTAL.name: None,
            }
        }
    }

    @staticmethod
    def get(repository_type: RepositoryType, database_type: DatabaseType, model: Model) -> Optional[Repository]:
        repository_type = RepositoryFacade.__repositories[repository_type.name][database_type.name][model.name]
        repository = repository_type() if repository_type else None
        LOG.info('Retrieving repository: {}'.format(repository))
        return repository

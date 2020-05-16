from src.core.enum.database_type import DatabaseType

from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.car_service import CarService
from src.core.service.customer_service import CustomerService
from src.core.service.employee_service import EmployeeService
from src.core.service.rental_service import RentalService
from src.core.service.service import Service
from src.core.tools import log_init
from src.main import Main

LOG = log_init(Main.log_file)


class ServiceFacade:
    __services = {
        RepositoryType.FILE.name: {
            DatabaseType.ARCHIVE.name: {
                Model.CAR.name: CarService(
                    RepositoryType.FILE, DatabaseType.ARCHIVE),
                Model.CUSTOMER.name: CustomerService(
                    RepositoryType.FILE, DatabaseType.ARCHIVE),
                Model.EMPLOYEE.name: EmployeeService(
                    RepositoryType.FILE, DatabaseType.ARCHIVE),
                Model.RENTAL.name: RentalService(
                    RepositoryType.FILE, DatabaseType.ARCHIVE),
            }
        },
        RepositoryType.DATABASE.name: {
            DatabaseType.MYSQL.name: {
                Model.CAR.name: CarService(
                    RepositoryType.DATABASE, DatabaseType.MYSQL),
                Model.CUSTOMER.name: CustomerService(
                    RepositoryType.DATABASE, DatabaseType.MYSQL),
                Model.EMPLOYEE.name: EmployeeService(
                    RepositoryType.DATABASE, DatabaseType.MYSQL),
                Model.RENTAL.name: RentalService(
                    RepositoryType.DATABASE, DatabaseType.MYSQL),
            },
            DatabaseType.POSTGRES.name: {
                Model.CAR.name: CarService(
                    RepositoryType.DATABASE, DatabaseType.POSTGRES),
                Model.CUSTOMER.name: CustomerService(
                    RepositoryType.DATABASE, DatabaseType.POSTGRES),
                Model.EMPLOYEE.name: EmployeeService(
                    RepositoryType.DATABASE, DatabaseType.POSTGRES),
                Model.RENTAL.name: RentalService(
                    RepositoryType.DATABASE, DatabaseType.POSTGRES),
            }
        }
    }

    @staticmethod
    def get(repository_type: RepositoryType, database_type: DatabaseType, model: Model) -> Service:
        service = ServiceFacade.__services[repository_type.name][database_type.name][model.name]
        LOG.info('Retrieving service: {}'.format(service))
        return service

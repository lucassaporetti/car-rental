from src.configs import AppConfigs
from src.core.enums.database_type import DatabaseType
from src.core.enums.model import Model
from src.core.enums.repository_type import RepositoryType
from src.core.services.car_service import CarService
from src.core.services.customer_service import CustomerService
from src.core.services.employee_service import EmployeeService
from src.core.services.rental_service import RentalService
from src.core.services.service import Service
from src.core.tools.commons import log_init

LOG = log_init(AppConfigs.log_file)


class ServiceFacade:
    __services = {
        Model.CAR.name: CarService,
        Model.CUSTOMER.name: CustomerService,
        Model.EMPLOYEE.name: EmployeeService,
        Model.RENTAL.name: RentalService,
    }

    @staticmethod
    def get(repository_type: RepositoryType, database_type: DatabaseType, model: Model) -> Service:
        service_type = ServiceFacade.__services[model.name]
        service = service_type(repository_type, database_type) if service_type else None
        LOG.info('Retrieving service: {}'.format(service))
        return service

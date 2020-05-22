from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.car_service import CarService
from src.core.service.customer_service import CustomerService
from src.core.service.employee_service import EmployeeService
from src.core.service.rental_service import RentalService
from src.core.service.service import Service
from src.core.tools.commons import log_init

LOG = log_init(AppConfigs.log_file())


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

    @staticmethod
    def get_car_service() -> Service:
        return ServiceFacade.get(AppConfigs.repository_type(), AppConfigs.database_type(), Model.CAR)

    @staticmethod
    def get_customer_service() -> Service:
        return ServiceFacade.get(AppConfigs.repository_type(), AppConfigs.database_type(), Model.CUSTOMER)

    @staticmethod
    def get_employee_service() -> Service:
        return ServiceFacade.get(AppConfigs.repository_type(), AppConfigs.database_type(), Model.EMPLOYEE)

    @staticmethod
    def get_rental_service() -> Service:
        return ServiceFacade.get(AppConfigs.repository_type(), AppConfigs.database_type(), Model.RENTAL)

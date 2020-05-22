from abc import ABC
from typing import Optional, Type

from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.factory.mysql.car_factory import CarFactory as MysqlCarFactory
from src.core.factory.mysql.customer_factory import CustomerFactory as MysqlCustomerFactory
from src.core.factory.mysql.employee_factory import EmployeeFactory as MysqlEmployeeFactory
from src.core.factory.mysql.rental_factory import RentalFactory as MysqlRentalFactory
from src.core.factory.sql_factory import SqlFactory
from src.core.tools.commons import log_init

LOG = log_init(AppConfigs.log_file())


class SqlFactoryFacade(ABC):
    __cache = {}
    __factories = {
        DatabaseType.MYSQL: {
            Model.CAR: MysqlCarFactory,
            Model.CUSTOMER: MysqlCustomerFactory,
            Model.EMPLOYEE: MysqlEmployeeFactory,
            Model.RENTAL: MysqlRentalFactory
        },
        DatabaseType.POSTGRES: {
            Model.CAR: None,
            Model.CUSTOMER: None,
            Model.EMPLOYEE: None,
            Model.RENTAL: None
        },
    }

    @staticmethod
    def create_or_get(factory_class: Type):
        cache_key = factory_class.__name__
        if cache_key in SqlFactoryFacade.__cache:
            LOG.info('Retrieving factory {}'.format(cache_key))
            return SqlFactoryFacade.__cache[cache_key]
        else:
            LOG.info('Creating factory {}'.format(cache_key))
            SqlFactoryFacade.__cache[cache_key] = factory_class()
            return SqlFactoryFacade.__cache[cache_key]

    @staticmethod
    def get(database_type: DatabaseType, model: Model) -> Optional[SqlFactory]:
        factory_class = SqlFactoryFacade.__factories[database_type][model]
        factory = SqlFactoryFacade.create_or_get(factory_class)
        return factory

import src.core.factory as factories

from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.factory.sql_factory import SqlFactory
from src.core.tools import log_init
from src.main import Main

LOG = log_init(Main.log_file)


class SqlFactoryFacade:
    __factories = {
        DatabaseType.MYSQL.name: {
            Model.CAR.name: factories.mysql.car_factory,
            Model.CUSTOMER.name: factories.mysql.customer_factory,
            Model.EMPLOYEE.name: factories.mysql.employee_factory,
            Model.RENTAL.name: factories.mysql.rental_factory
        },
        DatabaseType.POSTGRES.name: {
            Model.CAR.name: factories.postgres.car_factory,
            Model.CUSTOMER.name: factories.postgres.customer_factory,
            Model.EMPLOYEE.name: factories.postgres.employee_factory,
            Model.RENTAL.name: factories.postgres.rental_factory
        },
    }

    @staticmethod
    def get(database_type: DatabaseType, model: Model) -> SqlFactory:
        factory = SqlFactoryFacade.__factories[database_type.name][model.name]
        LOG.info('Retrieving factory: {}'.format(factory))
        return factory

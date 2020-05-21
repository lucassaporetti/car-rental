from typing import Optional

import src.core.factories as factories

from src.core.enums.database_type import DatabaseType
from src.core.enums.model import Model
from src.core.factories.sql_factory import SqlFactory
from src.app_configs import AppConfigs
from src.core.tools.commons import log_init

LOG = log_init(AppConfigs.log_file())


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
    def get(database_type: DatabaseType, model: Model) -> Optional[SqlFactory]:
        factory_type = SqlFactoryFacade.__factories[database_type.name][model.name]
        factory = factory_type() if factory_type else None
        LOG.info('Retrieving factory: {}'.format(factory))
        return factory

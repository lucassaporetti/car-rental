from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.repository.repository_facade import RepositoryFacade
from src.core.service.service import Service

from src.model.car import Car


class CarService(Service):
    def __init__(self, repository_type: RepositoryType, database_type: DatabaseType):
        super().__init__(RepositoryFacade.get(repository_type, database_type, Model.CAR))

    def save(self, car: Car):
        super().save(car)


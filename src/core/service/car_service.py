from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service import Service

from core.model.car import Car


class CarService(Service):
    def __init__(self, repository_type: RepositoryType, database_type: DatabaseType):
        super().__init__(repository_type, database_type, Model.CAR)

    def save(self, car: Car):
        super().save(car)

    def remove(self, car: Car):
        super().remove(car)

    def get(self, uuid: str) -> Car:
        entity = super().get(uuid)
        car = Car()
        car.__dict__ = entity.__dict__
        return car

from src.core.base.Repository import Repository
from src.models import Rental


class RentalRepository(Repository):
    def __init__(self):
        super().__init__("/home/musik/GIT-Repository/car-rental/data/rentals.dat")

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)


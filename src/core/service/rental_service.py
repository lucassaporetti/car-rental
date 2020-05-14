from src.core.base.service import Service
from src.core.repository.db.rental_repository import RentalRepository
from src.model import rental


class RentalService(Service):
    def __init__(self):
        super().__init__(RentalRepository())

    def save(self, rental: rental):
        super().save(rental)


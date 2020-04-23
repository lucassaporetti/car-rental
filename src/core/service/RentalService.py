from src.core.base.Service import Service
from src.core.repository.RentalRepository import RentalRepository
from src.models import Rental


class RentalService(Service):
    def __init__(self):
        super().__init__(RentalRepository())

    def save(self, rental: Rental):
        super().save(rental)


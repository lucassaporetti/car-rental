from src.core.repositories.file.file_repository import FileRepository
from core.config.app_configs import AppConfigs
from core.models.rental import Rental


class RentalRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{AppConfigs.root_dir()}/../data/rentals.dat")

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)

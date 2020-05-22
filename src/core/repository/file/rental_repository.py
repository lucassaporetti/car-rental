from src.core.repository.file.file_repository import FileRepository
from core.config.app_configs import AppConfigs
from core.model.rental import Rental


class RentalRepository(FileRepository):
    def __init__(self):
        super().__init__("{}/../data/rentals.dat".format(AppConfigs.root_dir()))

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)

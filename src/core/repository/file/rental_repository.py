from src.core.repository.file.file_repository import FileRepository
from src.main import Main
from src.model.rental import Rental


class RentalRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{Main.cur_dir}/../data/rentals.dat")

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)


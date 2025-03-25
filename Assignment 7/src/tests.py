from src.domain.complex_number import ComplexNumber
from src.repository.memory_repository import MemoryRepository
from src.services.services import Services


class Tests:
    @staticmethod
    def test_for_add_new_complex_number():
        repository = MemoryRepository()
        service = Services(repository)
        service.add_complex_number(2, 4)
        assert len(repository) == 11 # 10 default generated + 1 added
        assert repository[len(repository) - 1] == ComplexNumber(2, 4)


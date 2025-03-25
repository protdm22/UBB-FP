import copy

from src.domain.complex_number import ComplexNumber
from src.repository.repository import Repository

FIRST_NUMBER = 0


class Services:
    def __init__(self, repository: Repository):
        self.__repository = repository
        self.__history = []

    def add_complex_number(self, real_part, imaginary_part):
        """
        Calls the repository function to append a new complex number with a given real part and a given
        imaginary part to the list of complex numbers
        :param real_part: the given real part
        :param imaginary_part: the given imaginary part
        :return: None
        """
        self.save_current_state()
        complex_number = ComplexNumber(real_part, imaginary_part)
        self.__repository.add_complex_number(complex_number)

    def return_all_complex_numbers(self):
        return self.__repository.get_all_complex_numbers()

    def undo_last_operation(self):
        if not self.__history:
            print("UNDO ERROR! No operations to undo")
            return

        last_state = self.__history.pop()
        self.restore_state(last_state)

    def save_current_state(self):
        current_state = self.__repository.get_all_complex_numbers()
        self.__history.append(copy.deepcopy(current_state))

    def restore_state(self, state):
        for i in range(len(self.__repository)):
            self.__repository.remove_complex_number(0)
        for complex_number in state:
            self.__repository.add_complex_number(complex_number)

    def remove_numbers_on_positions_outside_interval(self, interval_start, interval_end):
        self.save_current_state()
        for i in range(interval_end, len(self.__repository)):
            self.__repository.remove_complex_number(interval_end)
        for i in range(interval_start - 1):
            self.__repository.remove_complex_number(FIRST_NUMBER)

    def list_length(self):
        return len(self.__repository)

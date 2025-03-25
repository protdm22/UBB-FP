from src.domain.complex_number import ComplexNumber


class Repository:

    def get_all_complex_numbers(self):
        ...

    def add_complex_number(self, complex_number: ComplexNumber):
        ...

    def remove_complex_number(self, index: int):
        ...

from random import randint

from src.domain.complex_number import ComplexNumber

MINIMUM_POSSIBLE_VALUE = -1000
MAXIMUM_POSSIBLE_VALUE = 1000

class GeneratorUtilities:
    @staticmethod
    def generate_random_complex_numbers(numbers_to_generate):
        list_of_complex_numbers = []

        for i in range(numbers_to_generate):
            real_part = randint(MINIMUM_POSSIBLE_VALUE, MAXIMUM_POSSIBLE_VALUE)
            imaginary_part = randint(MINIMUM_POSSIBLE_VALUE, MAXIMUM_POSSIBLE_VALUE)

            complex_number = ComplexNumber(real_part, imaginary_part)
            list_of_complex_numbers.append(complex_number)

        return list_of_complex_numbers

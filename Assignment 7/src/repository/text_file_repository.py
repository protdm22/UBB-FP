import os.path
from src.domain.complex_number import ComplexNumber
from src.repository.memory_repository import MemoryRepository

REAL_PART = 0
IMAGINARY_PART = 1

NUMBER_OF_TOKENS_FOR_COMPLEX_NUMBERS = 2


class TextFileRepository(MemoryRepository):
    def __init__(self, filename="data/complex_numbers.txt"):
        """
        Initialize the text file repository. Load data from the file if it exists,
        otherwise create a new file with randomly generated data.
        :param filename: The path to the text file used for storage.
        """
        super().__init__()
        self.__filename = filename
        if os.path.exists(self.__filename):
            self.__load_data()
        else:
            self.__save_data()

    def __load_data(self):
        """
        Load the repository's data from a text file.
        :return: None
        """
        self._data = []
        input_file = open(self.__filename, "rt")
        line = input_file.readline().strip()
        while line:
            tokens = line.split(":")
            if len(tokens) == NUMBER_OF_TOKENS_FOR_COMPLEX_NUMBERS:
                real_part = int(tokens[REAL_PART])
                imaginary_part = int(tokens[IMAGINARY_PART])
                complex_number = ComplexNumber(real_part, imaginary_part)
                self._data.append(complex_number)
            line = input_file.readline().strip()
        input_file.close()

    def __save_data(self):
        """
        Save the repository's data to a text file.
        :return: None
        """
        output_file = open(self.__filename, "wt")
        for complex_number in self._data:
            output_file.write(f"{complex_number.get_real_part()}:{complex_number.get_imaginary_part()}\n")
        output_file.close()

    def add_complex_number(self, complex_number: ComplexNumber):
        """
        Add a new complex number to the repository and save the state to a file.
        :param complex_number: An instance of ComplexNumber to add.
        :return: None
        """
        super().add_complex_number(complex_number)
        self.__save_data()

    def remove_complex_number(self, index):
        """
        Remove a complex number at a specified index and save the state to a file.
        :param index: The position of the complex number to remove.
        :return:
        """
        super().remove_complex_number(index)
        self.__save_data()

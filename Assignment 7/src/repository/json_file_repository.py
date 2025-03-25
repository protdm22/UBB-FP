import json
import os
from src.domain.complex_number import ComplexNumber
from src.repository.memory_repository import MemoryRepository


class JsonRepository(MemoryRepository):
    def __init__(self, filename="repository.json"):
        """
        Initialize the JSON file repository. Load data from the file if it exists,
        otherwise create a new file with randomly generated data.
        :param filename: The path to the JSON file used for storage.
        """
        super().__init__()
        self.__filename = filename
        if os.path.exists(self.__filename):
            self.__load_data()
        else:
            self.__save_data()

    def __load_data(self):
        """
        Load the repository's data from a JSON file.
        :return: None
        """
        input_file = open(self.__filename, "r")
        input_data = json.load(input_file)
        input_file.close()

        self._data = []
        for complex_number in input_data:
            self._data.append(ComplexNumber(complex_number['real_part'], complex_number['imaginary_part']))

    def __save_data(self):
        """
        Save the repository's data to a JSON file.
        :return: None
        """

        output_data = []
        for complex_number in self._data:
            output_data.append({
                "real_part": complex_number.get_real_part(),
                "imaginary_part": complex_number.get_imaginary_part()
            })

        output_file = open(self.__filename, "w")
        json.dump(output_data, output_file, indent=4)
        output_file.close()

    def add_complex_number(self, complex_number: ComplexNumber):
        """
        Add a new complex number to the repository and save the state to a JSON file.
        :param complex_number: An instance of ComplexNumber to add.
        :return: None
        """
        super().add_complex_number(complex_number)
        self.__save_data()

    def remove_complex_number(self, index):
        """
        Remove a complex number at a specified index and save the state to a JSON file.
        :param index: The position of the complex number to remove.
        :return: None
        """
        super().remove_complex_number(index)
        self.__save_data()

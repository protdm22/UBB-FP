import os.path
import pickle
from src.domain.complex_number import ComplexNumber
from src.repository.memory_repository import MemoryRepository


class BinaryFileRepository(MemoryRepository):
    def __init__(self, filename="data/complex_numbers.pickle"):
        """
        Initialize the binary file repository. Load data from the file if it exists,
        otherwise create a new file with randomly generated data.
        :param filename: The path to the binary file used for storage.
        """
        super().__init__()
        self.__filename = filename
        if os.path.exists(self.__filename):
            self.__load_data()
        else:
            self.__save_data()

    def __load_data(self):
        """
        Load the repository's data from a binary file.
        :return: None
        """
        file = open(self.__filename, "rb")
        self._data = pickle.load(file)
        file.close()

    def __save_data(self):
        """
        Save the repository's data to a binary file.
        :return: None
        """
        file = open(self.__filename, "wb")
        pickle.dump(self._data, file)
        file.close()

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
        :return: None
        """
        super().remove_complex_number(index)
        self.__save_data()

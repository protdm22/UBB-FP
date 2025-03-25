from src.domain.complex_number import ComplexNumber
from src.repository.repository import Repository
from src.utilities.generator_utilities import GeneratorUtilities

LOWER_BOUND = -1

INITIAL_INDEX = -1

NUMBER_OF_ELEMENTS_TO_GENERATE = 10

class RepositoryError(Exception):
    def __init__(self, error_message):
        """
        Initialize the RepositoryError with a specific error message.
        :param error_message: A string containing the error description.
        """
        self.__error_message = error_message

    def __str__(self):
        """
        Return a string representation of the error.
        :return: A formatted string indicating the repository error.
        """
        return "REPOSITORY ERROR: " + self.__error_message


class RepositoryIterator:
    def __init__(self, data):
        """
        Initialize the iterator with a data collection.
        :param data: A collection (list, dictionary, etc.) of elements to iterate over.
        """
        self.__data = data
        self.__index = INITIAL_INDEX

    def __next__(self):
        """
        Return the next element in the collection.
        :raises StopIteration: When there are no more elements to iterate over.
        """
        self.__index += 1
        if len(self.__data) - 1 == self.__index:
            raise StopIteration()
        return self.__data[self.__index]


class MemoryRepository(Repository):
    def __init__(self, filename=""):
        """
        Initialize the memory repository with randomly generated complex numbers.
        """
        self._data = GeneratorUtilities.generate_random_complex_numbers(NUMBER_OF_ELEMENTS_TO_GENERATE)

    def get_all_complex_numbers(self):
        """
        Retrieve all complex numbers in the repository.
        :return: A list of ComplexNumber instances.
        """
        return self._data

    def add_complex_number(self, complex_number: ComplexNumber):
        """
        Add a new complex number to the repository.
        :param complex_number: An instance of ComplexNumber to add.
        :return: None
        """
        self._data.append(complex_number)

    def remove_complex_number(self, index):
        """
        Remove a complex number at a specified index.
        :param index: The position of the complex number to remove.
        :return: The removed ComplexNumber instance.
        """
        return self._data.pop(index)

    def __len__(self):
        """
        Return the number of elements in the repository.
        :return: The count of elements in the repository.
        """
        return len(list(self._data))

    def __getitem__(self, index):
        """
        Retrieve the complex number at a specific index.
        :param index: The position of the complex number to retrieve.
        :return: The ComplexNumber at the specified index or None if out of bounds.
        """
        if LOWER_BOUND < index < len(self):
            return self._data[index]
        return None

    def __iter__(self):
        """
        Return an iterator for the repository data.
        :return: An instance of RepositoryIterator.
        """
        return RepositoryIterator([*self._data.values()])

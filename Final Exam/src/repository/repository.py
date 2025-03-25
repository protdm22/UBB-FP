from src.domain.sentence import Sentence


class Repository:
    def __init__(self):
        self.__data = {}
        self.__filename = "input.txt"
        self.__sentence_id = 1
        self.__load_data()

    def add(self, new_object):
        """
        Adds a new sentence to the repository
        :param new_object: the new sentence
        :return: None
        """
        self.__data[self.__sentence_id] = new_object
        self.__sentence_id += 1

    def __load_data(self):
        """
        Loads the sentences for the game from a file
        :return: None
        """
        input_file = open(self.__filename, "rt")
        lines = input_file.readlines()
        for line in lines:
            line = line.strip()
            sentence = Sentence(line)
            self.add(sentence)
        input_file.close()

    def get_all(self):
        return [*self.__data.values()]

class Sentence:
    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

    @property
    def words(self):
        return self.__text.split(' ')

    def __len__(self):
        return len(self.__text)

    def __str__(self):
        return self.__text

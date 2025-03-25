from random import randint, shuffle

from src.repository.repository import Repository


class ServiceException(Exception):
    pass


class UndoException(ServiceException):
    pass


class GameOver(ServiceException):
    pass


class GameLogic:
    def __init__(self, repository: Repository):
        self.__repository = repository
        self.__history = ""
        self.__sentence = ""

    def check_game_status(self, sentence, score):
        if sentence == self.__sentence:
            raise GameOver(f"You win! Your score is {score}")
        if score == 0:
            raise GameOver("Defeat :(")

    def swap(self, sentence, score, word1, word2, index1, index2):
        """
        Swaps the specified letters between two words and updates sentence and score
        :param sentence: The sentence with all words
        :param score: current score
        :param word1: index of first word
        :param word2: index of second word
        :param index1: index of the letter from the first word
        :param index2: index of the letter from the second word
        :return: modified sentence
                 updated score
        """
        self.record_undo(sentence)
        sentence = sentence.split(' ')
        final_sentence = ""
        w1 = word1
        w2 = word2
        word1 = sentence[word1]
        word2 = sentence[word2]
        word1, word2 = self.swap_letters(word1, word2, index1, index2)

        for i in range(len(sentence)):
            if i == w1:
                final_sentence += word1
            elif i == w2:
                final_sentence += word2
            else:
                final_sentence += sentence[i]
            if i != len(sentence) - 1:
                final_sentence += " "

        return final_sentence, score - 1

    def get_all_sentences(self):
        return self.__repository.get_all()

    @staticmethod
    def get_sentence_length(sentence):
        length = 0
        words_list = sentence.words
        for i in range(len(words_list)):
            length += len(words_list[i])
        return length

    def get_random_sentence(self):
        """
        Returns a random sentence from the repository
        :return: the random sentence
        """
        all_sentences = self.__repository.get_all()
        random_sentence = randint(0, (len(all_sentences) - 1))
        self.__sentence = all_sentences[random_sentence]
        return self.__sentence

    def get_shuffled_sentence(self):
        """
        Returns a shuffled sentence for the game start
        :return: the shuffled sentence
        """
        sentence = self.get_random_sentence()
        words_list = sentence.words
        final_sentence = ""

        if len(words_list) != 1:
            for i in range(0, len(words_list) - 1, 2):
                word1 = words_list[i]
                word2 = words_list[i + 1]
                if len(word1) > 2 and len(word2) > 2:
                    index1 = randint(1, len(word1) - 2)
                    index2 = randint(1, len(word2) - 2)
                    word1, word2 = self.swap_letters(word1, word2, index1, index2)
                final_sentence = final_sentence + word1 + " " + word2 + " "

            if len(words_list) % 2 == 1:
                final_sentence += words_list[len(words_list) - 1]

        else:
            if len(words_list[0]) > 3:
                index1 = randint(1, len(words_list[0]) - 2)
                char1 = words_list[0][index1]
                index2 = randint(1, len(words_list[0]) - 2)
                char2 = words_list[0][index2]
                final = ""
                for char in range(len(words_list[0])):
                    if char == index1:
                        final += char2
                    elif char == index2:
                        final += char1
                    else:
                        final += words_list[0][char]
                return final
            else:
                return words_list[0]

        return final_sentence

    @staticmethod
    def swap_letters(word1, word2, index1, index2):
        """
        Swaps two letters between two words
        :param word1: the first word
        :param word2: the second word
        :param index1: the index of the letter in the first word
        :param index2: the index of the letter in the second word
        :return: the words with swapped letters
        """
        new1 = ""
        new2 = ""
        char1 = word1[index1]
        char2 = word2[index2]

        for char in range(len(word1)):
            if char != index1:
                new1 += word1[char]
            else:
                new1 += char2

        for char in range(len(word2)):
            if char != char2:
                new2 += word2[char]
            else:
                new2 += char1

        return new1, new2

    def record_undo(self, state):
        self.__history = state

    def undo(self):
        if self.__history == "":
            raise UndoException("ERROR! No undoes available")
        aux = self.__history
        self.__history = ""
        return aux

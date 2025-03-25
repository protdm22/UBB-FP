import unittest

from src.domain.sentence import Sentence
from src.repository.repository import Repository
from src.service.game_logic import GameLogic


class Tests(unittest.TestCase):
    def test_add(self):
        repo = Repository()
        test_sentence = Sentence("test")
        repo.add(test_sentence)
        all_sentences = repo.get_all()
        self.assertEqual(str(all_sentences[5]), "test")

    def test_get_all(self):
        repo = Repository()
        all_sentences = repo.get_all()
        self.assertEqual(str(all_sentences[0]), "scramble")
        self.assertEqual(str(all_sentences[1]), "Dream without fear")
        self.assertEqual(str(all_sentences[2]), "The quick brown fox jumps over the lazy dog")
        self.assertEqual(str(all_sentences[3]), "You can win")
        self.assertEqual(str(all_sentences[4]), "Work hard dream big")

    def test_swap_letters(self):
        repo = Repository()
        logic = GameLogic(repo)

        all_sentences = repo.get_all()
        sentence = str(all_sentences[3])
        sentence = sentence.split(' ')
        word1 = sentence[0]
        word2 = sentence[1]
        a, b = logic.swap_letters(word1, word2, 1, 1)
        self.assertEqual(("Yau", "can"), (a, b))

    def test_sentence_length(self):
        repo = Repository()
        logic = GameLogic(repo)

        sentence = Sentence("Anna has apples")
        length = logic.get_sentence_length(sentence)  # Length is without spaces
        self.assertEqual(length, 13)


if __name__ == "__main__":
    test = Tests()
    unittest.main()

from src.domain.sentence import Sentence
from src.service.game_logic import GameLogic, ServiceException, GameOver


class UI:
    def __init__(self, game_logic: GameLogic):
        self.__game_logic = game_logic

    @staticmethod
    def print_current_state(sentence, score):
        print(sentence, f"[score is: {score}]")

    def game_loop(self):

        sentence = self.__game_logic.get_shuffled_sentence()
        sent = Sentence(sentence)
        score = self.__game_logic.get_sentence_length(sent)

        while True:
            try:
                self.__game_logic.check_game_status(sentence, score)
            except GameOver as ge:
                print(ge)
                break
            self.print_current_state(sentence, score)
            try:
                user_choice = input(">>> ")
                if user_choice == "quit":
                    break

                user_choice = user_choice.split(' ')

                if user_choice[0].strip() == "swap":
                    if len(user_choice) != 6:
                        raise ValueError("ERROR! Invalid input format")
                    word1 = int(user_choice[1])
                    index1 = int(user_choice[2])
                    if user_choice[3] != "-":
                        raise ValueError("ERROR! Invalid input format")
                    word2 = int(user_choice[4])
                    index2 = int(user_choice[5])
                    sentence, score = self.__game_logic.swap(sentence, score, word1, word2, index1, index2)

                elif user_choice[0].strip() == "undo":
                    sentence = self.__game_logic.undo()

                else:
                    print("ERROR! Unknown option")

            except ServiceException as se:
                print(se)
            except ValueError as ve:
                print(ve)

from src.repository.repository import Repository
from src.service.game_logic import GameLogic
from src.ui.ui import UI


class Game:
    @staticmethod
    def game_start():
        repository = Repository()
        game_logic = GameLogic(repository)
        ui = UI(game_logic)
        ui.game_loop()


if __name__ == "__main__":
    game = Game()
    game.game_start()

from src.repository import Repository
from src.services import Services
from src.ui import UI


class Application:
    @staticmethod
    def start():
        repository = Repository("repository.txt")
        service = Services(repository)
        ui = UI(service)
        ui.menu()


if __name__ == "__main__":
    application = Application()
    application.start()

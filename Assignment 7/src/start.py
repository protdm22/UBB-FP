from src.repository.binary_file_repository import BinaryFileRepository
from src.repository.json_file_repository import JsonRepository
from src.repository.memory_repository import MemoryRepository
from src.repository.text_file_repository import TextFileRepository
from src.services.services import Services
from src.tests import Tests
from src.ui.ui import UI, UIError

COMMENT_INDEX_ON_CURRENT_LINE = 0

SETTING = 0
SETTING_VALUE = 1


class Start:
    def __init__(self):
        self.__repository_type = "memory"
        self.__filename = ""

    def load_settings(self):
        settings_file = open("settings.properties", "rt")
        settings = settings_file.readlines()

        for line in settings:
            line = line.strip()
            if line[COMMENT_INDEX_ON_CURRENT_LINE] != '#':
                line = line.split('=')

                setting = line[SETTING]
                setting_value = line[SETTING_VALUE]

                if setting == "complex_numbers":
                    self.__filename = setting_value.strip('\"')
                elif setting == "repository":
                    self.__repository_type = setting_value

        settings_file.close()

    def start_program(self):
        repositories_dictionary = {
            "memory": MemoryRepository,
            "text": TextFileRepository,
            "binary": BinaryFileRepository,
            "json": JsonRepository
        }

        repository = repositories_dictionary[self.__repository_type](self.__filename)

        service = Services(repository)
        ui = UI(service)

        Tests.test_for_add_new_complex_number()

        while True:
            try:
                ui.menu()
            except UIError as error_message:
                print(error_message)


if __name__ == "__main__":
    start = Start()
    start.load_settings()
    start.start_program()

from src.domain.discipline import Discipline
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.binary_file_repository import BinaryFileRepository
from src.repository.memory_repository import MemoryRepository
from src.repository.repository import Repository
from src.repository.repository_exceptions import RepositoryException
from src.repository.text_file_repository import TextFileRepository
from src.services.discipline_service import DisciplineService
from src.services.grade_service import GradeService
from src.services.service_exceptions import ServiceException
from src.services.statistics_service import StatisticsService
from src.services.student_service import StudentService
from src.services.undo_redo_service import UndoError, UndoRedoService, RedoError
from src.ui.ui import UIException
from src.ui.ui import UI

INDEX_OF_COMMENT_INDICATOR = 0

SETTING = 0
SETTING_VALUE = 1


class Application:
    def __init__(self):
        self.__students_filename = ""
        self.__grades_filename = ""
        self.__disciplines_filename = ""
        self.__repository_type = "memory"

    def load_settings(self):

        settings_file = open("settings.properties", "rt")
        settings = settings_file.readlines()

        for line in settings:
            line = line.strip()
            if line[INDEX_OF_COMMENT_INDICATOR] != '#':
                line = line.split('=')

                setting = line[SETTING]
                setting_value = line[SETTING_VALUE]

                if setting == "students":
                    self.__students_filename = setting_value.strip('\"')
                elif setting == "grades":
                    self.__grades_filename = setting_value.strip('\"')
                elif setting == "disciplines":
                    self.__disciplines_filename = setting_value.strip('\"')
                elif setting == "repository":
                    self.__repository_type = setting_value

        settings_file.close()

    def start_application(self):
        repositories_dictionary = {
            "memory": MemoryRepository,
            "text": TextFileRepository,
            "binary": BinaryFileRepository
        }

        student_repository = repositories_dictionary[self.__repository_type](self.__students_filename, Student)
        discipline_repository = repositories_dictionary[self.__repository_type](self.__disciplines_filename, Discipline)
        grade_repository = repositories_dictionary[self.__repository_type](self.__grades_filename, Grade)

        undo_redo_service = UndoRedoService()

        student_service = StudentService(student_repository, grade_repository, undo_redo_service)
        discipline_service = DisciplineService(discipline_repository, grade_repository, undo_redo_service)
        grade_service = GradeService(student_repository, discipline_repository, grade_repository, undo_redo_service)
        statistics_service = StatisticsService(student_repository, discipline_repository, grade_repository)

        ui = UI(student_service, discipline_service, grade_service, statistics_service, undo_redo_service)

        while True:
            try:
                ui.main_menu()
            except UIException as ui_error_message:
                print(ui_error_message)
            except UndoError as undo_error_message:
                print(undo_error_message)
            except RedoError as redo_error_message:
                print(redo_error_message)
            except RepositoryException as repository_error_message:
                print(repository_error_message)
            except ServiceException as service_error_message:
                print(service_error_message)
            except ValueError as value_error_message:
                print(value_error_message)


if __name__ == "__main__":
    application = Application()
    application.load_settings()
    application.start_application()

from random import randint

from src.domain.grade import Grade
from src.repository.repository import Repository
from src.services.service_exceptions import IDNotFoundException
from src.utilities.generator_utilities import GeneratorUtilities

NO_ELEMENTS = 0

ID_MINIMUM_VALUE = 500
ID_MAXIMUM_VALUE = 999999


class GradeService:
    def __init__(self, student_repository: Repository, discipline_repository: Repository, grade_repository: Repository):
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__grade_repository = grade_repository

        if len(self.__grade_repository) == NO_ELEMENTS:
            list_of_random_grades = GeneratorUtilities.generate_random_grades(500, self.__student_repository,
                                                                              self.__discipline_repository)
            for grade in list_of_random_grades:
                new_grade = Grade(grade.id, grade.student_id, grade.discipline_id, grade.value)
                self.__grade_repository.add_entry(new_grade)

    def add_grade(self, student_id, discipline_id, grade_value):
        grade_id = randint(ID_MINIMUM_VALUE, ID_MAXIMUM_VALUE)
        while self.__grade_repository.find_entry_by_id(grade_id):
            grade_id = randint(ID_MINIMUM_VALUE, ID_MAXIMUM_VALUE)
        new_grade = Grade(str(grade_id), student_id, discipline_id, grade_value)
        self.__grade_repository.add_entry(new_grade)

    def return_all_grades(self):
        return self.__grade_repository.get_all_entries()

    def is_student_id_valid(self, student_id):
        if not self.__student_repository.find_entry_by_id(student_id):
            raise IDNotFoundException(f"No student with ID={student_id} exists")

    def is_discipline_id_valid(self, discipline_id):
        if not self.__discipline_repository.find_entry_by_id(discipline_id):
            raise IDNotFoundException(f"No discipline with ID={discipline_id} exists")

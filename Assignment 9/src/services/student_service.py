from src.domain.student import Student
from src.repository.repository import Repository
from src.services.service_exceptions import NoMatchingSearches
from src.services.undo_redo_service import FunctionCall, Operation, CascadedOperation
from src.utilities.generator_utilities import GeneratorUtilities

NO_ELEMENTS = 0

NUMBER_OF_STUDENTS_TO_GENERATE = 20


class StudentService:
    def __init__(self, student_repository: Repository, grade_repository: Repository, undo_redo_service):
        self.__student_repository = student_repository
        self.__grade_repository = grade_repository
        self.__undo_redo_service = undo_redo_service

        if len(self.__student_repository) == NO_ELEMENTS:
            list_of_random_students = GeneratorUtilities.generate_random_students(NUMBER_OF_STUDENTS_TO_GENERATE)
            for student in list_of_random_students:
                new_student = Student(student.name, student.id)
                self.__student_repository.add_entry(new_student)

    def add_student(self, new_student_name, new_student_id):
        """
        Adds a new Student entry in the repository
        :param new_student_name: the name of the new student
        :param new_student_id: the id of the new student
        :return: None
        """
        new_student = Student(new_student_name, new_student_id)
        self.__student_repository.add_entry(new_student)

        redo_add_student_function = FunctionCall(self.__student_repository.add_entry, new_student)
        undo_add_student_function = FunctionCall(self.__student_repository.remove_entry, new_student_id)
        self.__undo_redo_service.record_undo(Operation(undo_add_student_function, redo_add_student_function))

    def remove_student(self, student_id):
        """
        Removes the student with the given id from the repository
        :param student_id: the id of the student
        :return: None
        """
        redo_remove_student_function = FunctionCall(self.__student_repository.remove_entry, student_id)
        undo_remove_student_function = FunctionCall(
            self.__student_repository.add_entry, self.__student_repository.find_entry_by_id(student_id))
        undo_redo_operations = [Operation(undo_remove_student_function, redo_remove_student_function)]

        self.__student_repository.remove_entry(student_id)

        list_of_all_grades = self.__grade_repository.get_all_entries()
        for grade in list_of_all_grades:
            if grade.student_id == student_id:
                redo_add_student_grade_function = FunctionCall(self.__grade_repository.remove_entry, grade.id)
                undo_add_student_grade_function = FunctionCall(self.__grade_repository.add_entry, grade)
                undo_redo_operations.append(Operation(undo_add_student_grade_function, redo_add_student_grade_function))

                self.__grade_repository.remove_entry(grade.id)

        self.__undo_redo_service.record_undo(CascadedOperation(*undo_redo_operations))

    def update_student(self, student_id, new_student_name):
        """
        Updates the name of a student with a given ID in the repository
        :param student_id: the ID of the student
        :param new_student_name: the new name of the student
        :return: None
        """
        redo_update_student_function = FunctionCall(self.__student_repository.update_entry, student_id,
                                                    new_student_name)
        undo_update_student_function = FunctionCall(self.__student_repository.update_entry, student_id,
                                                    self.__student_repository.find_entry_by_id(student_id).name)
        self.__undo_redo_service.record_undo(Operation(undo_update_student_function, redo_update_student_function))

        self.__student_repository.update_entry(student_id, new_student_name)

    def return_all_students(self):
        """
        Returns a list of all the students from the repository
        :return: the list of all students
        """
        return self.__student_repository.get_all_entries()

    def search_for_students(self, student_to_search):
        list_of_matching_students = []
        list_of_all_students = self.__student_repository.get_all_entries()

        for student in list_of_all_students:
            if student_to_search in student.id:
                list_of_matching_students.append(student)

        if len(list_of_matching_students) != NO_ELEMENTS:
            return list_of_matching_students

        for student in list_of_all_students:
            if student_to_search.lower() in student.name.lower():
                list_of_matching_students.append(student)

        if len(list_of_matching_students) != NO_ELEMENTS:
            return list_of_matching_students
        else:
            raise NoMatchingSearches("No matching students found")

    def return_student_by_id(self, student_id):
        return self.__student_repository.find_entry_by_id(student_id)

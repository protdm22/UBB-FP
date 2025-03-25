from random import randint

from src.domain import Assignment
from src.repository import Repository

MINIMUM_REQUIRED_STUDENT_NAME_LENGTH = 3
EMPTY_STRING = 0

MIN_ID = 1
MAX_ID = 9


class ServiceException(Exception):
    pass


class NameTooShortException(ServiceException):
    pass


class NoAssignmentSolutionGivenException(ServiceException):
    pass


class Services:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_assignment(self, student_name, assignment_solution):
        """
        Adds a new assignment to the repository
        :param student_name: the name of the student whose assignment it is
        :param assignment_solution: the student's solution to the assignment
        :return: None
        """
        if len(student_name) < MINIMUM_REQUIRED_STUDENT_NAME_LENGTH:
            raise NameTooShortException("INVALID INPUT! The student's name must be at least 3 characters long")
        if len(assignment_solution) == EMPTY_STRING:
            raise NoAssignmentSolutionGivenException("INVALID INPUT! No solution given")

        assignment_id = randint(MIN_ID, MAX_ID)
        while self.__repository.find_entry_by_id(assignment_id):
            assignment_id = randint(MIN_ID, MAX_ID)

        new_assignment = Assignment(assignment_id, student_name, assignment_solution)
        self.__repository.add_entry(new_assignment)

    def return_all_assignments(self):
        return self.__repository.get_all_entries()

    def dishonesty_check(self):
        list_of_all_assignments = self.__repository.get_all_entries()
        list_of_all_assignments_to_check = self.__repository.get_all_entries()
        list_of_dishonest_students = []

        for assignment in list_of_all_assignments:
            current_assignment_words = assignment.solution.split(' ')
            current_assignment_word_count = len(current_assignment_words)

            for assignment_to_check in list_of_all_assignments_to_check:
                copied_words = 0
                if assignment_to_check.id != assignment.id:
                    current_assignment_to_check_words = assignment_to_check.solution.split(' ')
                    for word_to_check in current_assignment_to_check_words:
                        for word in current_assignment_words:
                            if word_to_check == word:
                                copied_words += 1
                    if copied_words *100 // current_assignment_word_count>20:
                        list_of_dishonest_students.append((assignment_to_check.student_name,assignment.student_name,copied_words *100 // current_assignment_word_count))

        return list_of_dishonest_students
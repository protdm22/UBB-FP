from src.domain.discipline import Discipline
from src.domain.student import Student

NO_GRADES = 0
PASSING_GRADE = 5
DEFAULT_GRADE = 0

NO_STUDENTS = 0
FIRST_PLACE = 0

TWO_DECIMALS = 2

NO_DISCIPLINES = 0
FIRST_POSITION_IN_THE_LIST = 0


class StudentSituationDataTransferObject:
    def __init__(self, student: Student, average_grade: float):
        self.__student = student
        self.__average_grade = average_grade

    @property
    def average_grade(self):
        return self.__average_grade

    def __str__(self):
        return f"Student {self.__student.name} has an average grade of {self.__average_grade}"


class DisciplineAverageGradeDataTransferObject:
    def __init__(self, discipline: Discipline, average_grade):
        self.__discipline = discipline
        self.__average_grade = average_grade

    @property
    def average_grade(self):
        return self.__average_grade

    def __str__(self):
        return f"The average for '{self.__discipline.name}' is {self.__average_grade}"


class StatisticsService:
    def __init__(self, student_repository, discipline_repository, grade_repository):
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__grade_repository = grade_repository

    @staticmethod
    def calculate_student_average_grade_at_given_discipline(student: Student, discipline: Discipline,
                                                            list_of_all_grades):
        discipline_average = DEFAULT_GRADE
        discipline_number_of_grades = NO_GRADES

        for grade in list_of_all_grades:

            if grade.student_id == student.id and grade.discipline_id == discipline.id:
                discipline_number_of_grades += 1
                discipline_average += grade.value

        if discipline_number_of_grades != NO_GRADES:
            discipline_average = round(discipline_average / discipline_number_of_grades, TWO_DECIMALS)

        return discipline_number_of_grades, discipline_average

    def check_if_student_is_failing(self, student: Student, list_of_all_disciplines, list_of_all_grades):
        for discipline in list_of_all_disciplines:

            discipline_number_of_grades, discipline_average = self.calculate_student_average_grade_at_given_discipline(
                student, discipline, list_of_all_grades)

            if discipline_number_of_grades != NO_GRADES and discipline_average < PASSING_GRADE:
                return True

        return False

    def return_all_failing_students(self):
        list_of_failing_students = []
        list_of_all_students = self.__student_repository.get_all_entries()
        list_of_all_disciplines = self.__discipline_repository.get_all_entries()
        list_of_all_grades = self.__grade_repository.get_all_entries()

        for student in list_of_all_students:

            student_is_failing = self.check_if_student_is_failing(student, list_of_all_disciplines, list_of_all_grades)
            if student_is_failing:
                list_of_failing_students.append(student)

        return list_of_failing_students

    def calculate_student_aggregated_average_grade(self, student: Student, list_of_all_disciplines, list_of_all_grades):
        student_average_grade = DEFAULT_GRADE
        number_of_disciplines_where_student_has_grades = NO_GRADES

        for discipline in list_of_all_disciplines:

            discipline_number_of_grades, discipline_average = self.calculate_student_average_grade_at_given_discipline(
                student, discipline, list_of_all_grades)

            if discipline_number_of_grades != NO_GRADES:
                student_average_grade += discipline_average
                number_of_disciplines_where_student_has_grades += 1

        return round(student_average_grade / number_of_disciplines_where_student_has_grades, TWO_DECIMALS)

    @staticmethod
    def position_to_insert_at(average_grade, list_of_ordered_objects) -> int:
        number_of_objects = len(list_of_ordered_objects)

        if number_of_objects == NO_STUDENTS:
            return FIRST_POSITION_IN_THE_LIST

        if average_grade < list_of_ordered_objects[number_of_objects - 1].average_grade:
            return number_of_objects

        object_index = FIRST_POSITION_IN_THE_LIST
        current_object = list_of_ordered_objects[object_index]

        while current_object.average_grade > average_grade and object_index < number_of_objects - 1:
            object_index += 1
            current_object = list_of_ordered_objects[object_index]

        return object_index

    def return_students_with_best_situations(self):
        list_of_best_students = []
        list_of_all_students = self.__student_repository.get_all_entries()
        list_of_all_disciplines = self.__discipline_repository.get_all_entries()
        list_of__all_grades = self.__grade_repository.get_all_entries()

        for student in list_of_all_students:
            student_average_grade = self.calculate_student_aggregated_average_grade(student, list_of_all_disciplines,
                                                                                    list_of__all_grades)
            temporary_student_rank = self.position_to_insert_at(student_average_grade, list_of_best_students)
            list_of_best_students.insert(temporary_student_rank,
                                         StudentSituationDataTransferObject(student, student_average_grade))

        return list_of_best_students

    @staticmethod
    def calculate_discipline_average_grade(discipline: Discipline, list_of_all_grades):
        average_grade = DEFAULT_GRADE
        number_of_grades = NO_GRADES

        for grade in list_of_all_grades:
            if grade.discipline_id == discipline.id:
                average_grade += grade.value
                number_of_grades += 1

        if number_of_grades != NO_GRADES:
            average_grade = round(average_grade / number_of_grades, TWO_DECIMALS)

        return number_of_grades, average_grade

    def return_disciplines_in_descending_order_of_average_grade(self):
        list_of_disciplines_sorted_by_average_grade = []
        list_of_all_disciplines = self.__discipline_repository.get_all_entries()
        list_of_all_grades = self.__grade_repository.get_all_entries()

        for discipline in list_of_all_disciplines:
            number_of_grades, average_grade = self.calculate_discipline_average_grade(discipline, list_of_all_grades)

            if number_of_grades != NO_GRADES:
                discipline_index_in_the_list = self.position_to_insert_at(average_grade,
                                                                          list_of_disciplines_sorted_by_average_grade)
                list_of_disciplines_sorted_by_average_grade.insert(discipline_index_in_the_list,
                                                                   DisciplineAverageGradeDataTransferObject(discipline,
                                                                                                            average_grade))

        return list_of_disciplines_sorted_by_average_grade

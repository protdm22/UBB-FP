from src.domain.grade import Grade
from src.repository.repository import Repository

NUMBER_OF_OPTIONS_FOR_MAIN_MENU = 5
NUMBER_OF_OPTIONS_FOR_MANAGE_MENU = 4

FIRST_OPTION = 1

OPTION_MANAGE_STUDENTS = 1
OPTION_MANAGE_DISCIPLINES = 2
OPTION_GRADE = 3
OPTION_SEARCH_STUDENTS = 4
OPTION_SEARCH_DISCIPLINES = 5

OPTION_ADD = 1
OPTION_REMOVE = 2
OPTION_UPDATE = 3
OPTION_LIST = 4

NO_ELEMENTS = 0


class UIException(Exception):
    def __init__(self, error_details):
        self._error_message = "UI ERROR! " + error_details

    def __str__(self):
        return self._error_message


class UI:
    def __init__(self, student_service, discipline_service, grade_service):
        self.__student_service = student_service
        self.__discipline_service = discipline_service
        self.__grade_service = grade_service

    def print_main_menu(self):
        print("########################################")
        print("[1] Manage students")
        print("[2] Manage disciplines")
        print("[3] Grade students")
        print("[4] Search for students")
        print("[5] Search for disciplines")
        print("########################################")
        print("Choose an option:")

    def print_manage_menu(self, thing_to_manage):
        print(f"[1] Add a new {thing_to_manage}")
        print(f"[2] Remove a {thing_to_manage}")
        print(f"[3] Update {thing_to_manage}")
        print(f"[4] List all {thing_to_manage}s")

    def request_user_option(self, maximum_number_of_options):
        while True:
            try:
                option = int(input(">>> "))
                if option < FIRST_OPTION or option > maximum_number_of_options:
                    raise UIException("Option not recognised")
                return option
            except ValueError:
                raise ValueError("INPUT ERROR! Please enter an integer number!!!")
            except UIException:
                raise UIException("Option not recognised")

    def manage_students_menu(self):
        self.print_manage_menu("student")
        manage_option = self.request_user_option(NUMBER_OF_OPTIONS_FOR_MANAGE_MENU)

        if manage_option == OPTION_ADD:
            student_to_add_name = input("Enter the name of the new student: ")
            student_to_add_id = input("Enter an ID for the new student: ")
            self.__student_service.add_student(student_to_add_name, student_to_add_id)
            print(f"Student '{student_to_add_name}' with ID={student_to_add_id} has been successfully added!")

        elif manage_option == OPTION_REMOVE:
            student_to_remove = input("Enter the ID of the student you would like to remove: ")
            self.__student_service.remove_student(student_to_remove)
            print(f"Student with ID={student_to_remove} has been successfully removed!")

        elif manage_option == OPTION_UPDATE:
            student_to_update = input("Enter the ID of the student you would like to update: ")
            updated_student = input(f"Enter the new name for the student with ID = {student_to_update}: ")
            self.__student_service.update_student(student_to_update, updated_student)
            print(f"Student with ID={student_to_update} has been successfully updated!")

        elif manage_option == OPTION_LIST:
            list_of_students_to_print = self.__student_service.return_all_students()
            for student in list_of_students_to_print:
                print(str(student))

    def manage_disciplines_menu(self):
        self.print_manage_menu("discipline")
        manage_option = self.request_user_option(NUMBER_OF_OPTIONS_FOR_MANAGE_MENU)

        if manage_option == OPTION_ADD:
            discipline_to_add_name = input("Enter the name of the new discipline: ")
            discipline_to_add_id = input("Enter an ID for the new discipline: ")
            self.__discipline_service.add_discipline(discipline_to_add_name, discipline_to_add_id)
            print(f"Discipline '{discipline_to_add_name}' with ID={discipline_to_add_id} has been successfully added!")

        elif manage_option == OPTION_REMOVE:
            discipline_to_remove = input("Enter the ID of the discipline you would like to remove: ")
            self.__discipline_service.remove_discipline(discipline_to_remove)
            print(f"Discipline with ID={discipline_to_remove} has been successfully removed!")


        elif manage_option == OPTION_UPDATE:
            discipline_to_update = input("Enter the ID of the discipline you would like to update: ")
            updated_discipline = input(f"Enter the new name for the discipline with ID = {discipline_to_update}: ")
            self.__discipline_service.update_discipline(discipline_to_update, updated_discipline)
            print(f"Discipline with ID={discipline_to_update} has been successfully updated!")

        elif manage_option == OPTION_LIST:
            list_of_disciplines_to_print = self.__discipline_service.return_all_disciplines()
            for discipline in list_of_disciplines_to_print:
                print(str(discipline))

    def main_menu(self):
        self.print_main_menu()
        main_option = self.request_user_option(NUMBER_OF_OPTIONS_FOR_MAIN_MENU)

        if main_option == OPTION_MANAGE_STUDENTS:
            self.manage_students_menu()

        elif main_option == OPTION_MANAGE_DISCIPLINES:
            self.manage_disciplines_menu()

        elif main_option == OPTION_GRADE:

            student_id = input("Enter the ID of the student you would like to grade: ")
            self.__grade_service.is_student_id_valid(student_id)

            student = self.__student_service.return_student_by_id(student_id)

            all_grades = self.__grade_service.return_all_grades()
            student_grades = []
            for grade in all_grades:
                if grade.student_id == student_id:
                    student_grades.append(grade)

            if len(student_grades) != NO_ELEMENTS:
                print(f"Student {student.name} has the following grades:")
                for grade in student_grades:
                    print(
                        f"{str(grade)} at {self.__discipline_service.return_discipline_by_id(grade.discipline_id).name}")
            else:
                print(f"Student {student.name} has no grades")

            discipline_id = input("Enter the ID of the discipline where you would like to grade: ")
            self.__grade_service.is_discipline_id_valid(discipline_id)
            print(
                f"Grading {student.name} at discipline '{self.__discipline_service.return_discipline_by_id(discipline_id).name}':")

            try:
                grade = float(input("Enter the grade: "))
            except ValueError:
                raise ValueError("INPUT ERROR! The grade must be a rational value!")

            if not 0 <= grade <= 10:
                raise ValueError("INPUT ERROR! The grade value must be between 0 and 10")

            self.__grade_service.add_grade(student_id, discipline_id, grade)



        elif main_option == OPTION_SEARCH_STUDENTS:
            student_to_search = input("Enter the name or ID of the student you would like to search for: ")
            list_of_matching_students = self.__student_service.search_for_students(student_to_search)
            for student in list_of_matching_students:
                print(str(student))

        elif main_option == OPTION_SEARCH_DISCIPLINES:
            discipline_to_search = input("Enter the name or ID of the discipline you would like to search for: ")
            list_of_matching_disciplines = self.__discipline_service.search_for_disciplines(discipline_to_search)
            for discipline in list_of_matching_disciplines:
                print(str(discipline))

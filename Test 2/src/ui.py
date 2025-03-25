from src.services import Services, ServiceException

OPTION_ADD_ASSIGNMENT = "1"
OPTION_SHOW_ASSIGNMENTS = "2"
OPTION_DISHONESTY_CHECK = "3"


class UI:
    def __init__(self, service: Services):
        self.__service = service

    @staticmethod
    def print_menu():
        print("[1] Add a new assignment")
        print("[2] Show all assignments")
        print("[3] Dishonesty check")

    @staticmethod
    def request_input_for_add_assignment():
        student_name = input("Enter the name of the new student: ")
        assignment_solution = input(f"Enter {student_name}'s solution: ")
        return student_name, assignment_solution

    def menu(self):
        while True:
            try:
                self.print_menu()

                menu_option = input(">>> ").strip()

                if menu_option == OPTION_ADD_ASSIGNMENT:
                    student_name, assignment_solution = self.request_input_for_add_assignment()
                    self.__service.add_assignment(student_name, assignment_solution)

                elif menu_option == OPTION_SHOW_ASSIGNMENTS:
                    list_of_all_assignments = self.__service.return_all_assignments()
                    list_of_all_assignments.sort(key=lambda current_assignment: current_assignment.id)
                    for assignment in list_of_all_assignments:
                        print(assignment)

                elif menu_option == OPTION_DISHONESTY_CHECK:
                    list_of_frauds = self.__service.dishonesty_check()
                    for fraud, original, procent in list_of_frauds:
                        print(f"{fraud} -> {original},({procent}% of {original}'s solution)")

            except ValueError as value_error_message:
                print(value_error_message)
            except ServiceException as service_error_message:
                print(service_error_message)

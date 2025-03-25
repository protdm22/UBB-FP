OPTION_ADD = "1"
OPTION_DISPLAY = "2"
OPTION_FILTER = "3"
OPTION_UNDO = "4"

LOWER_BOUND_OF_LIST = 1

from src.services.services import Services


class UIError(Exception):
    def __init__(self, error_message):
        self.__error_message = error_message

    def __str__(self):
        return "INPUT ERROR: " + self.__error_message


class UI:
    def __init__(self, service: Services):
        self.__service = service

    def print_menu(self):
        print("#########################################")
        print("[1] Add a new complex number")
        print("[2] Display the list of all complex numbers")
        print("[3] Filter the list between start and end")
        print("[4] Undo")
        print("Choose your option:")

    def menu(self):
        self.print_menu()
        user_choice = input(">>> ")

        if user_choice == OPTION_ADD:
            real_part, imaginary_part = self.request_input_for_add_complex_number()

            self.__service.add_complex_number(real_part, imaginary_part)

        elif user_choice == OPTION_DISPLAY:
            list_of_complex_numbers = self.__service.return_all_complex_numbers()
            for i in range(len(list_of_complex_numbers)):
                print(f"{i + 1}: {list_of_complex_numbers[i]}")


        elif user_choice == OPTION_FILTER:
            interval_start, interval_end = self.request_input_for_filter()
            self.__service.remove_numbers_on_positions_outside_interval(interval_start, interval_end)

        elif user_choice == OPTION_UNDO:
            self.__service.undo_last_operation()

        else:
            raise UIError("Option not found")

    def request_input_for_add_complex_number(self):
        try:
            real_part = int(input("Enter the real part for the new complex number: "))
        except ValueError:
            raise UIError("The real part must be an integer!")

        try:
            imaginary_part = int(input("Enter the imaginary part for the new complex number: "))
        except ValueError:
            raise UIError("The imaginary part must be an integer!")

        return real_part, imaginary_part

    def request_input_for_filter(self):
        try:
            interval_start = int(input("Enter the interval start: "))
        except ValueError:
            raise UIError("The interval start must be an integer!")

        upper_bound_of_list = self.__service.list_length()

        if interval_start < LOWER_BOUND_OF_LIST or interval_start > upper_bound_of_list:
            raise UIError("The interval start is not a valid position in the list")

        try:
            interval_end = int(input("Enter the interval end: "))
        except ValueError:
            raise UIError("The interval end must be an integer!")

        if interval_end < LOWER_BOUND_OF_LIST or interval_end > upper_bound_of_list:
            raise UIError("The interval end is not a valid position in the list")

        if interval_end < interval_start:
            interval_start, interval_end = interval_end, interval_start

        return interval_start, interval_end

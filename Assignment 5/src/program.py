#
# Write the implementation for A5 in this file
#
"""
Set A - 1. Determine the length and the elements of a longest subarray of distinct numbers.
Set B - 2. Determine the length and the elements of a longest increasing subsequence,
           when considering each number's real part.
"""
from random import randint

ROW_OF_HASHES = "#################################"
REAL_PART = 0
IMAGINARY_PART = 1
NUMBER_OF_PREDEFINED_COMPLEX_NUMBERS = 10


#
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def return_complex_number(real_part: int, imaginary_part: int):
    return [real_part, imaginary_part]


def get_real_part(complex_number):
    return complex_number[REAL_PART]


def get_imaginary_part(complex_number):
    return complex_number[IMAGINARY_PART]


def set_real_part(complex_number, new_real_part):
    complex_number[REAL_PART] = new_real_part


def set_imaginary_part(complex_number, new_imaginary_part):
    complex_number[IMAGINARY_PART] = new_imaginary_part


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


# def return_complex_number(real_part: int, imaginary_part: int):
#     return {"real_part": real_part, "imaginary_part": imaginary_part}
#
#
# def get_real_part(complex_number):
#     return complex_number["real_part"]
#
#
# def get_imaginary_part(complex_number):
#     return complex_number["imaginary_part"]
#
#
# def set_real_part(complex_number, new_real_part):
#     complex_number["real_part"] = new_real_part
#
#
# def set_imaginary_part(complex_number, new_imaginary_part):
#     complex_number["imaginary_part"] = new_imaginary_part


# Functions independent of representations that do not fit into other categories :)

def complex_number_to_string(complex_number) -> str:
    if get_imaginary_part(complex_number) == 0:
        return str(get_real_part(complex_number))
    else:
        if get_real_part(complex_number) == 0:
            return f"{get_imaginary_part(complex_number)}i"
        elif get_imaginary_part(complex_number) < 0:
            return f"{get_real_part(complex_number)}{get_imaginary_part(complex_number)}i"
        else:
            return f"{get_real_part(complex_number)}+{get_imaginary_part(complex_number)}i"


def set_ordinal_indicator(index: int) -> str:
    if index % 100 // 10 != 1:
        if index % 10 == 1:
            return str(index) + "st"
        elif index % 10 == 2:
            return str(index) + "nd"
        elif index % 10 == 3:
            return str(index) + "rd"
        else:
            return str(index) + "th"
    else:
        return str(index) + "th"


def generate_initial_complex_numbers(list_of_complex_numbers):
    for i in range(NUMBER_OF_PREDEFINED_COMPLEX_NUMBERS):
        real_part = randint(-100, 100)
        imaginary_part = randint(-100, 100)
        list_of_complex_numbers.append(return_complex_number(real_part, imaginary_part))


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def longest_subarray_of_distinct_numbers(list_of_complex_numbers) -> list:
    """
    Function that returns a list of complex numbers that represent the longest subarray of
    distinct numbers of the given list of complex numbers
    :param list_of_complex_numbers: the given list of complex numbers
    :return: a list representing the longest subarray of distinct numbers
    """
    current_longest_subarray = []
    longest_subarray = []
    longest_subarray_maximum_length = 0

    for i in range(len(list_of_complex_numbers)):
        current_complex_number = list_of_complex_numbers[i]
        if current_complex_number not in current_longest_subarray:
            current_longest_subarray.append(current_complex_number)
        else:
            if len(current_longest_subarray) > longest_subarray_maximum_length:
                longest_subarray_maximum_length = len(current_longest_subarray)
                longest_subarray = current_longest_subarray.copy()
            current_longest_subarray = [list_of_complex_numbers[i]]

    if len(current_longest_subarray) > longest_subarray_maximum_length:
        longest_subarray = current_longest_subarray.copy()

    return longest_subarray


def longest_increasing_subsequence_by_real_part(list_of_complex_numbers):
    """
    Function that returns a list of complex numbers that represent the longest increasing
    subsequence considering the real part of the complex numbers from the given list of complex numbers
    :param list_of_complex_numbers: the given list of complex numbers
    :return: a list representing the longest increasing subsequence considering the real part
    of the complex numbers
    """

    dynamic_maximum_length_of_subsequence = [1 for _ in range(len(list_of_complex_numbers))]
    generated_subsequences = [-1 for _ in range(len(list_of_complex_numbers))]

    for current_position in range(1, len(list_of_complex_numbers)):
        for previous_position in range(0, current_position):
            if get_real_part(list_of_complex_numbers[current_position]) > get_real_part(
                    list_of_complex_numbers[previous_position]) and \
                    dynamic_maximum_length_of_subsequence[current_position] < dynamic_maximum_length_of_subsequence[
                previous_position] + 1:
                dynamic_maximum_length_of_subsequence[current_position] = dynamic_maximum_length_of_subsequence[
                                                                              previous_position] + 1
                generated_subsequences[current_position] = previous_position

    length_of_longest_subsequence = dynamic_maximum_length_of_subsequence[0]
    position_of_the_last_element_of_the_subsequence = 0

    for current_position in range(1, len(dynamic_maximum_length_of_subsequence)):
        if dynamic_maximum_length_of_subsequence[current_position] > length_of_longest_subsequence:
            length_of_longest_subsequence = dynamic_maximum_length_of_subsequence[current_position]
            position_of_the_last_element_of_the_subsequence = current_position

    longest_increasing_subsequence = []
    current_position_in_subsequence = position_of_the_last_element_of_the_subsequence

    while current_position_in_subsequence != -1:
        longest_increasing_subsequence.append(list_of_complex_numbers[current_position_in_subsequence])
        current_position_in_subsequence = generated_subsequences[
            current_position_in_subsequence]

    longest_increasing_subsequence.reverse()

    return longest_increasing_subsequence


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#


def read_list_of_complex_numbers(list_of_complex_numbers):
    print("How many complex numbers would you like to read?")
    while True:
        try:
            number_of_complex_numbers_to_read = int(input(">>> "))
            break
        except ValueError:
            print("Please enter a natural value!")
    for index in range(1, number_of_complex_numbers_to_read + 1):
        while True:
            try:
                real_part = int(
                    input(f"Enter the real part of the {set_ordinal_indicator(index)} complex number: "))
                break
            except ValueError:
                print("Please enter an integer value!")
        while True:
            try:
                imaginary_part = int(
                    input(f"Enter the imaginary part of the {set_ordinal_indicator(index)} complex number: "))
                break
            except ValueError:
                print("Please enter an integer value!")
        list_of_complex_numbers += [return_complex_number(real_part, imaginary_part)]


def print_list_of_complex_numbers(list_of_complex_numbers):
    for i in range(len(list_of_complex_numbers)):
        print(
            f"The {set_ordinal_indicator(i + 1)} element is {complex_number_to_string(list_of_complex_numbers[i])}")


def print_longest_subarray_of_distinct_numbers(list_of_complex_numbers):
    longest_subarray = longest_subarray_of_distinct_numbers(list_of_complex_numbers)
    print(f"The longest subarray of distinct has {len(longest_subarray)} elements:")
    print_list_of_complex_numbers(longest_subarray)


def print_longest_subsequence_of_increasing_numbers_by_real_part(list_of_complex_numbers):
    longest_subsequence = longest_increasing_subsequence_by_real_part(list_of_complex_numbers)
    print(f"The longest subsequence of increasing numbers considering the real part has {len(longest_subsequence)} elements:")
    print_list_of_complex_numbers(longest_subsequence)


def print_menu():
    print(ROW_OF_HASHES * 3)
    print("Menu options:")
    print(" read_list - Read a list of complex numbers from the console")
    print(" print_list - Print the current list of complex numbers")
    print(" longest_subarray - Print the longest subarray of distinct numbers")
    print(" longest_subsequence - Print a longest increasing subsequence (considering each number's real part)")
    print(" exit - Quit the program")
    print(ROW_OF_HASHES * 3)


def menu(list_of_complex_numbers: list):
    menu_options = {
        "read_list": read_list_of_complex_numbers,
        "print_list": print_list_of_complex_numbers,
        "longest_subarray": print_longest_subarray_of_distinct_numbers,
        "longest_subsequence": print_longest_subsequence_of_increasing_numbers_by_real_part
    }

    while True:
        print_menu()
        option = input(">>> ").lower()
        if option in menu_options:
            menu_options[option](list_of_complex_numbers)
        elif option == "exit":
            break
        elif option == "":
            continue
        else:
            print("Command not found")


def test_area():
    complex_test = return_complex_number(3, 4)
    assert get_real_part(complex_test) == 3
    assert get_imaginary_part(complex_test) == 4

    complex_test = return_complex_number(0, 0)
    set_real_part(complex_test, 3)
    set_imaginary_part(complex_test, 4)
    assert get_real_part(complex_test) == 3
    assert get_imaginary_part(complex_test) == 4
    assert complex_number_to_string(complex_test) == "3+4i"


if __name__ == "__main__":
    test_area()
    list_of_complex_numbers = []
    generate_initial_complex_numbers(list_of_complex_numbers)
    menu(list_of_complex_numbers)

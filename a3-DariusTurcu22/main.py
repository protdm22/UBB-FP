import random

OPTION_EXIT = 0
OPTION_SHOW_LIST = 1
OPTION_GENERATE_RANDOM_LIST = 2
OPTION_EXPONENTIAL_SEARCH = 3
OPTION_COCKTAIL_SORT = 4
OPTION_COMB_SORT = 5
OPTION_BEST_CASE = 6
OPTION_AVERAGE_CASE = 7
OPTION_WORST_CASE = 8

BEST_CASE = 10
AVERAGE_CASE = 11
WORST_CASE = 12

NOT_FOUND = -1

ROW_OF_HASHTAGS = "###########################################################"


def read_natural_number() -> int:
    """
    Function that returns an input only if it is a natural number
    :return: natural number
    """
    while True:
        try:
            input_value = int(input(">>> "))
            if input_value < 0:
                raise ValueError()
            return input_value
        except ValueError:
            print("Invalid value! Please enter a natural number!")


def generate_ascending_list(size: int) -> list:
    """
    Function that generates a list of natural numbers in ascending order
    :param size: natural number
    :return: list of natural numbers
    """
    best_case_list = list(range(size))
    return best_case_list


def generate_descending_list(size: int) -> list:
    """
        Function that generates a list of natural numbers in descending order
        :param size: natural number
        :return: list of natural numbers
        """
    worst_case_list = list(range(size, 0, -1))
    return worst_case_list


def generate_list_of_random_numbers(size: int) -> list:
    """
    Function that generates a list of n random natural numbers
    :param size: natural number
    :return: None
    """
    list_of_natural_numbers = []
    for i in range(size):
        list_of_natural_numbers.append(random.randint(0, 1000))
    return list_of_natural_numbers


def check_if_list_is_sorted(list_of_natural_numbers: list) -> bool:
    """
    Function that checks is a list arr is sorted in ascending order
    :param list_of_natural_numbers: list of natural numbers
    :return: boolean
    """
    for i in range(len(list_of_natural_numbers) - 1):
        if list_of_natural_numbers[i] > list_of_natural_numbers[i + 1]:
            return False
    return True


def print_best_case_for_all_algorithms() -> None:
    """
    Function that calls the function that draws a table comparing the time it takes to run each algorithm for each of their best cases on sets of data with exponential sizes
    :return: none
    """
    print("Best case (values are in milliseconds):\n" + ROW_OF_HASHTAGS)
    draw_efficiency_table_for_all_algorithms(BEST_CASE)


def print_average_case_for_all_algorithms() -> None:
    """
        Function that calls the function that draws a table comparing the time it takes to run each algorithm for each of their average cases on sets of data with exponential sizes
        :return: none
        """
    print("Average case (values are in milliseconds):\n" + ROW_OF_HASHTAGS)
    draw_efficiency_table_for_all_algorithms(AVERAGE_CASE)


def print_worst_case_for_all_algorithms() -> None:
    """
        Function that calls the function that draws a table comparing the time it takes to run each algorithm for each of their worst cases on sets of data with exponential sizes
        :return: none
        """
    print("Worst case (values are in milliseconds):\n" + ROW_OF_HASHTAGS)
    draw_efficiency_table_for_all_algorithms(WORST_CASE)


def exponential_search(list_of_natural_numbers: list, item_to_search: int) -> int:
    """
    Function that uses exponential search to find the index of a natural number item_to_search
    :param list_of_natural_numbers: list of natural numbers
    :param item_to_search: natural number
    :return: natural number (index)

    Time complexity:
        - Best case: O(1) - first element
            - the algorithm doesn't enter the first while loop, then left=0, right=1.
            In the next while loop, middle=0 and the value is found on list[middle]
            Therefore, its time complexity is O(1).
        - Average case: O(log(n))
        - Worst case: O(log(n)) - last element
            - the bound will first be the largest value of bound=2^n which is less than
            or equal to the size of the list => log(n)
            - binary search is then performed on the bounds (bound,list_size) => log(n)
            ==> log(n) + log(n), which in the big O-notation is log(n)
    """
    list_size = len(list_of_natural_numbers)
    if list_size == 0:
        return NOT_FOUND
    bound = 1
    while bound < list_size and list_of_natural_numbers[bound] < item_to_search:
        bound *= 2

    # binary search
    left = bound // 2
    right = min(bound, list_size - 1)
    while left <= right:
        middle = (left + right) // 2
        if item_to_search == list_of_natural_numbers[middle]:
            return middle
        elif item_to_search < list_of_natural_numbers[middle]:
            right = middle - 1
        elif item_to_search > list_of_natural_numbers[middle]:
            left = middle + 1
    return NOT_FOUND


def ask_for_step() -> int:
    """
    Function that prompts the user to input the parameter step
    :return: natural number
    """
    print("Please enter the value of the parameter step:")
    return read_natural_number()


def check_step(list_of_natural_numbers: list, step, step_counter, current_step: int) -> int:
    """
    Function that prints the list arr for every n steps, and increments step_ct otherwise
    :param list_of_natural_numbers: list of natural numbers
    :param step: natural number
    :param step_counter: natural number
    :param current_step: natural number
    :return: natural number
    """
    if step_counter != step:
        step_counter += 1
    if step_counter == step:
        print("Step", current_step, list_of_natural_numbers)
        step_counter = 0
    return step_counter


def cocktail_sort(list_to_be_sorted: list, step: int) -> None:
    """
    Function that uses cocktail sort to sort the list arr in ascending order
    :param step: natural number
    :param list_to_be_sorted: list of natural numbers
    :return: None

    Time complexity:
        - Best case: O(n) - ascending list
            - if the list is parsed from left to right the first time
            and no swaps are made (meaning that the list is already sorted)
            the algorithm exits => one parse through n elements
        - Average case: O(n^2)
        - Worst case: -O(n^2) = n+(n-1)+...+2+1 = n(n+1)/2 = n^2 - descending list
    """
    begin_index = 0
    end_index = len(list_to_be_sorted) - 1
    step_counter = 0
    current_step = 0
    swapped = False
    while begin_index <= end_index:
        new_begin_index = end_index
        new_end_index = begin_index
        for i in range(begin_index, end_index):
            if list_to_be_sorted[i] > list_to_be_sorted[i + 1]:
                list_to_be_sorted[i], list_to_be_sorted[i + 1] = list_to_be_sorted[i + 1], \
                    list_to_be_sorted[i]
                swapped = True
                if step >= 1:
                    current_step += 1
                    step_counter = check_step(list_to_be_sorted, step, step_counter, current_step)
            new_end_index = i
        end_index = new_end_index
        if not swapped:
            break
        swapped = False
        for i in range(end_index, begin_index, -1):
            if list_to_be_sorted[i] < list_to_be_sorted[i - 1]:
                list_to_be_sorted[i], list_to_be_sorted[i - 1] = list_to_be_sorted[i - 1], \
                    list_to_be_sorted[i]
                if step >= 1:
                    current_step += 1
                    step_counter = check_step(list_to_be_sorted, step, step_counter, current_step)
            new_begin_index = i
        begin_index = new_begin_index


def comb_sort(list_to_be_sorted: list, step: int) -> None:
    """
    Function that uses comb sort to sort the list arr in ascending order
    :param step: natural number
    :param list_to_be_sorted: list of natural numbers
    :return: None

    Time complexity:
        - Best case: O(nlog(n)) - ascending list
            - for an already sorted list, the gap will decrease exponentially by 1.3
            ==> log(1.3) and then very few swaps will be left when gap becomes 1
        - Average case: O((n^2)/(2^p))
        - Worst case: O(n^2) - descending list
            - The gap will become 1 when most of the list will not be sorted yet, and
            then it will behave like bubble sort, which has the complexity of n^2
    """
    length = len(list_to_be_sorted)
    gap = length
    shrink_factor = 1.3
    is_sorted = False
    step_counter = 0
    current_step = 0
    while not is_sorted:
        gap = int(gap // shrink_factor)
        if gap <= 1:
            gap = 1
            is_sorted = True
        index = 0
        while index + gap < length:
            if list_to_be_sorted[index] > list_to_be_sorted[index + gap]:
                list_to_be_sorted[index], list_to_be_sorted[index + gap] = list_to_be_sorted[index + gap], \
                    list_to_be_sorted[index]
                is_sorted = False
                if step >= 1:
                    current_step += 1
                    step_counter = check_step(list_to_be_sorted, step, step_counter, current_step)
            index += 1


def draw_efficiency_table_for_all_algorithms(case: int) -> None:
    """
    Function that draws a table comparing the time it takes to run each algorithm for each of their best/average/worst cases (depending on the input of the parameter case) on sets of data with exponential sizes
    :param case: natural number (either 1,2 or 3)
    :return: none
    """
    import timeit
    import texttable

    sort_functions = [comb_sort, cocktail_sort]
    list_sizes = [500, 1000, 2000, 4000, 8000]

    efficiency_table = texttable.Texttable()
    efficiency_table.add_row(['Functions/size'] + list_sizes)

    for sort_function in sort_functions:
        efficiency_table_row = [sort_function.__name__]
        for list_size in list_sizes:
            list_to_sort = []
            if case == BEST_CASE:
                list_to_sort = generate_ascending_list(list_size)
            elif case == AVERAGE_CASE:
                list_to_sort = generate_list_of_random_numbers(list_size)
            elif case == WORST_CASE:
                list_to_sort = generate_descending_list(list_size)
            execution_time = int(
                timeit.timeit(lambda: sort_function(list_to_sort, -1), number=1) * 1000
            )
            efficiency_table_row.append(execution_time)
        efficiency_table.add_row(efficiency_table_row)

    efficiency_table_row = [exponential_search.__name__]
    for list_size in list_sizes:
        array_to_search = generate_list_of_random_numbers(list_size)
        array_to_search.sort()
        if case == BEST_CASE:
            to_be_searched = array_to_search[0]
        elif case == AVERAGE_CASE:
            to_be_searched = array_to_search[random.randint(0, list_size - 1)]
        elif case == WORST_CASE:
            to_be_searched = array_to_search[list_size - 1]
        execution_time = int(
            timeit.timeit(lambda: exponential_search(array_to_search, to_be_searched), number=1) * 1000
        )
        efficiency_table_row.append(execution_time)
    efficiency_table.add_row(efficiency_table_row)

    print(efficiency_table.draw())


def print_menu() -> None:
    """
    Function that displays the menu options
    :return: None
    """
    print(ROW_OF_HASHTAGS + "\nMenu options:")
    print("[" + str(OPTION_SHOW_LIST) + "] Display the list")
    print("[" + str(OPTION_GENERATE_RANDOM_LIST) + "] Generate a list of n random natural numbers")
    print("[" + str(OPTION_EXPONENTIAL_SEARCH) + "] Search for an item in the list")
    print("[" + str(OPTION_COCKTAIL_SORT) + "] Sort the list using cocktail sort")
    print("[" + str(OPTION_COMB_SORT) + "] Sort the list using comb sort")
    print("[" + str(OPTION_BEST_CASE) + "] Best case for all algorithms")
    print("[" + str(OPTION_AVERAGE_CASE) + "] Average case for all algorithms")
    print("[" + str(OPTION_WORST_CASE) + "] Worst case for all algorithms")
    print("\n[" + str(OPTION_EXIT) + "] Exit")
    print(ROW_OF_HASHTAGS + "\nChoose an option:")


def menu(numbers_list: list) -> None:
    """
    Function that prompts the user to input their desired option and calls that respective function
    :param numbers_list: empty list that the function will work with
    :return: None
    """
    bad_command = False
    while True:
        if bad_command:
            print("Invalid option! Please enter a number between 0 and 5")
            bad_command = False
        else:
            print_menu()
        option = read_natural_number()
        if option == OPTION_EXIT:  # Exit
            break
        elif option == OPTION_SHOW_LIST:  # Show list
            if not numbers_list:
                print("The list is empty. Please consider generating a list first!")
            else:
                print(numbers_list)
        elif option == OPTION_GENERATE_RANDOM_LIST:  # Generate list
            print("Please enter the size of the list you would like to generate:")
            list_size = read_natural_number()
            numbers_list = generate_list_of_random_numbers(list_size)
            print("The list has been generated successfully!")
        elif option == OPTION_EXPONENTIAL_SEARCH:  # Exponential search
            if check_if_list_is_sorted(numbers_list):
                print("Please enter the number you would like to search for:")
                to_be_searched = read_natural_number()
                index_of_the_searched_number = exponential_search(numbers_list, to_be_searched)
                if index_of_the_searched_number == NOT_FOUND:
                    print("The element", to_be_searched, "was not found in the list.")
                else:
                    print("The element", to_be_searched, "can be found at index",
                          str(index_of_the_searched_number) + ".")
            else:
                print(
                    "The list is not sorted! Please sort the list using option [4] or [5] before searching for an element.")
        elif option == OPTION_COCKTAIL_SORT:  # Cocktail sort
            step = ask_for_step()
            cocktail_sort(numbers_list, step)
        elif option == OPTION_COMB_SORT:  # Comb sort
            step = ask_for_step()
            comb_sort(numbers_list, step)
        elif option == OPTION_BEST_CASE:  # Best case
            print_best_case_for_all_algorithms()
        elif option == OPTION_AVERAGE_CASE:  # Average case
            print_average_case_for_all_algorithms()
        elif option == OPTION_WORST_CASE:  # Worst case
            print_worst_case_for_all_algorithms()
        else:
            bad_command = True


def main():
    numbers_list = []
    menu(numbers_list)


main()

"""
    ########################################################
    Case for exponential search that takes more than 0ms :)
    ########################################################
    search_arr = generate_ascending_list(100000000)
    execution_time = int(timeit.timeit(lambda: exponential_search(search_arr, search_arr[len(search_arr)-1]), number=1)*1000)
    print(execution_time)
    ########################################################
"""

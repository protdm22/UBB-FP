""""""
"""
--- Backtracking ---
11. Two natural numbers m and n are given. Display in all possible
modalities the numbers from 1 to n, such that between any two numbers
on consecutive positions, the difference in absolute value is at least m.
If there is no solution, display a message.
"""

USE_ITERATIVE_BACKTRACKING = 1
USE_RECURSIVE_BACKTRACKING = 2

PURPOSE_READ_PERMUTATION_ORDER_AND_DIFFERENCE = 3
PURPOSE_SELECT_OPTION = 4


def read_natural_number(display_message: str, purpose: int) -> int:
    """
    Function that returns an input only if it is a natural number
    :return: natural number
    """
    while True:
        try:
            input_value = int(input(display_message))
            if input_value < 0:
                raise ValueError()
            return input_value
        except ValueError:
            if purpose == PURPOSE_READ_PERMUTATION_ORDER_AND_DIFFERENCE:
                print("Invalid input! Please enter valid values for m and n (natural numbers)!")
            if purpose == PURPOSE_SELECT_OPTION:
                print("Invalid input! Please enter a valid option!")


def check_if_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions(
        current_permutation: list,
        user_input_difference_between_numbers_on_consecutive_positions: int) -> bool:
    """
    Function that checks whether the absolute difference between any numbers on consecutive positions from the list current_permutation is at least user_input_difference_between_numbers_on_consecutive_positions
    :param current_permutation:
    :param user_input_difference_between_numbers_on_consecutive_positions:
    :return:
    """
    if len(current_permutation) > 1 and abs(current_permutation[-1] - current_permutation[
        -2]) < user_input_difference_between_numbers_on_consecutive_positions:
        return False
    return True


def is_final_permutation_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions(
        current_permutation: list, user_input_permutation_order) -> bool:
    """
    Function that checks whether all numbers of a given order have been used in current_permutation, hence being a solution, or not
    :param current_permutation: list of natural numbers (partial or complete permutation of numbers 1 to n)
    :param user_input_permutation_order: natural number
    :return: True or False
    """
    return len(current_permutation) == user_input_permutation_order


def final_permutation_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__found(
        current_permutation: list, solutions: list) -> None:
    """
    Function that prints and appends to the list of solutions the current_permutation because it is a solution (this function is only called if the is_solution function returns True)
    :param current_permutation:
    :param solutions:
    :return:
    """
    print(current_permutation)
    solutions.append(current_permutation)


# Iterative backtracking implementation
def generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_iterative(
        current_permutation: list, user_input_difference_between_numbers_on_consecutive_positions: int,
        user_input_permutation_order: int, used_numbers: set,
        solutions: list) -> None:
    """
    Function that uses an iterative implementation of the backtracking algorithm to
    generate all permutations of numbers from 1 to n that meet the conditions (the absolute difference between any
    numbers on consecutive positions from the list current_permutation is at least user_input_difference_between_numbers_on_consecutive_positions)
    :param current_permutation: list of natural numbers
    :param user_input_difference_between_numbers_on_consecutive_positions: natural number
    :param user_input_permutation_order: natural number
    :param used_numbers: set of natural numbers
    :param solutions: list of lists of natural numbers
    :return: None
    """
    current_number = 0
    current_permutation.append(0)
    while current_number + 1 > 0:
        permutation_found = False
        while not permutation_found and current_permutation[current_number] <= user_input_permutation_order:
            current_permutation[current_number] += 1
            if current_permutation[current_number] not in used_numbers and current_permutation[
                current_number] <= user_input_permutation_order and check_if_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions(
                current_permutation, user_input_difference_between_numbers_on_consecutive_positions):
                permutation_found = True
                used_numbers.add(current_permutation[current_number])
        if not permutation_found:
            current_permutation.pop()
            current_number -= 1
            if current_number + 1 > 0:
                used_numbers.remove(current_permutation[current_number])
        elif current_number + 1 < user_input_permutation_order:
            current_number += 1
            current_permutation.append(0)
        else:
            final_permutation_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__found(
                current_permutation, solutions)
            used_numbers.remove(current_permutation[current_number])


def generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_recursive(
        current_permutation: list, user_input_difference_between_numbers_on_consecutive_positions: int,
        user_input_permutation_order: int, used_numbers: set,
        solutions: list) -> None:
    """
    Function that uses a recursive implementation of the backtracking algorithm to
    generate all permutations of a given order that meet the conditions (the absolute difference between any
    numbers on consecutive positions from the list current_permutation is at least user_input_difference_between_numbers_on_consecutive_positions)
    :param current_permutation: list of natural numbers
    :param user_input_difference_between_numbers_on_consecutive_positions: natural number
    :param user_input_permutation_order: natural number
    :param used_numbers: set of natural numbers
    :param solutions: list of lists of natural numbers
    :return: None
    """
    if is_final_permutation_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions(
            current_permutation, user_input_permutation_order):
        final_permutation_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__found(
            current_permutation, solutions)
    else:
        for current_number in range(1, user_input_permutation_order + 1):
            if current_number not in used_numbers:
                current_permutation.append(current_number)
                used_numbers.add(current_number)
                if check_if_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions(
                        current_permutation, user_input_difference_between_numbers_on_consecutive_positions):
                    generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_recursive(
                        current_permutation, user_input_difference_between_numbers_on_consecutive_positions,
                        user_input_permutation_order, used_numbers, solutions)
                current_permutation.pop()
                used_numbers.remove(current_number)


# Recursive backtracking implementation


"""
    Time complexity for both algorithms is O(k^n), where n=user_input_permutation_order and k is the number
    of valid solutions, depending on the value of user_input_difference_between_numbers_on_consecutive_positions
"""

"""
#################################################################################################
Tested the stack method to quickly convert the algorithm from recursive to iterative backtracking
#################################################################################################

def backtracking_iterative_stack(current_permutation: list, user_input_difference_between_numbers_on_consecutive_positions: int, user_input_permutation_order: int,
                                 used_numbers: set, solutions: list) -> None:
    
    stack = [(current_permutation, used_numbers)]
    while len(stack) > 0:
        stack_current_permutation, stack_used_numbers = stack.pop()
        if is_solution(stack_current_permutation, user_input_permutation_order):
            solution_found(stack_current_permutation, solutions)
        else:
            for current_number in range(1, user_input_permutation_order + 1):
                if current_number not in stack_used_numbers:
                    stack_current_permutation.append(current_number)
                    stack_used_numbers.add(current_number)
                    if current_permutation_meets_conditions(stack_current_permutation, user_input_difference_between_numbers_on_consecutive_positions):
                        stack.append((stack_current_permutation.copy(), stack_used_numbers.copy()))
                    stack_current_permutation.pop()
                    stack_used_numbers.remove(current_number)
"""


def choose_backtracking_implementation(initial_permutation: list,
                                       user_input_difference_between_numbers_on_consecutive_positions: int,
                                       user_input_permutation_order: int,
                                       initial_used_numbers: set, solutions: list) -> None:
    """
    Function that prompts the user to choose whether to use the iterative or the recursive implementation of the backtracking algorithm used for solving the given problem
    :param initial_permutation: empty list
    :param user_input_difference_between_numbers_on_consecutive_positions: natural number
    :param user_input_permutation_order: natural number
    :param initial_used_numbers: empty set
    :param solutions: empty list
    :return: None
    """
    print("Choose which type of implementation you would like to use:")
    print("[" + str(USE_ITERATIVE_BACKTRACKING) + "] Iterative backtracking")
    print("[" + str(USE_RECURSIVE_BACKTRACKING) + "] Recursive backtracking")
    user_input = read_natural_number(">>> ", PURPOSE_SELECT_OPTION)
    if user_input == USE_ITERATIVE_BACKTRACKING:
        generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_iterative(
            initial_permutation, user_input_difference_between_numbers_on_consecutive_positions,
            user_input_permutation_order, initial_used_numbers, solutions)
    elif user_input == USE_RECURSIVE_BACKTRACKING:
        generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_recursive(
            initial_permutation, user_input_difference_between_numbers_on_consecutive_positions,
            user_input_permutation_order, initial_used_numbers, solutions)
    else:
        print("Invalid option!")
        choose_backtracking_implementation(initial_permutation,
                                           user_input_difference_between_numbers_on_consecutive_positions,
                                           user_input_permutation_order, initial_used_numbers, solutions)


def test_backtracking(initial_permutation: list, user_input_difference_between_numbers_on_consecutive_positions: int,
                      user_input_permutation_order: int,
                      initial_used_numbers: set, solutions: list) -> None:
    """
    Function that calls both implementations of backtracking for the given problem in order to test their outputs
    :param initial_permutation: empty list
    :param user_input_difference_between_numbers_on_consecutive_positions: natural number
    :param user_input_permutation_order: natural number
    :param initial_used_numbers: empty set
    :param solutions: empty list
    :return: None
    """
    print("\nIterative version:")
    generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_iterative(
        initial_permutation, user_input_difference_between_numbers_on_consecutive_positions,
        user_input_permutation_order, initial_used_numbers, solutions)
    print("\nRecursive version:")
    generate_all_permutations_of_order__user_input_permutation_order__where_the_absolute_difference_of_numbers_on_consecutive_positions_is_at_least__user_input_difference_between_numbers_on_consecutive_positions__backtracking_recursive(
        initial_permutation, user_input_difference_between_numbers_on_consecutive_positions,
        user_input_permutation_order, initial_used_numbers, solutions)


def backtracking_main():
    """
    The main function for the backtracking part of this assignment
    :return: None
    """
    solutions = []
    user_input_difference_between_numbers_on_consecutive_positions = read_natural_number(
        "Enter the value of the difference between numbers on consecutive positions = ",
        PURPOSE_READ_PERMUTATION_ORDER_AND_DIFFERENCE)
    user_input_permutation_order = read_natural_number("Enter the order of the permutations = ",
                                                       PURPOSE_READ_PERMUTATION_ORDER_AND_DIFFERENCE)
    # choose_backtracking_implementation([], user_input_difference_between_numbers_on_consecutive_positions, user_input_permutation_order, set(), solutions)
    test_backtracking([], user_input_difference_between_numbers_on_consecutive_positions, user_input_permutation_order,
                      set(), solutions)
    if not solutions:
        print("No solutions found")


backtracking_main()

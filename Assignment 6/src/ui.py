#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import copy

FIRST_COMMAND = 0

LOWEST_SCORE_ALLOWED = 0
HIGHEST_SCORE_ALLOWED = 10

PROBLEM1_SCORE = 0
PROBLEM2_SCORE = 1
PROBLEM3_SCORE = 2

PROBLEM1 = "P1"
PROBLEM2 = "P2"
PROBLEM3 = "P3"

NUMBER_OF_PARAMETERS_FOR_ADD = 3

NUMBER_OF_PARAMETERS_FOR_INSERT = 5

AT_KEYWORD_PARAMETER_FOR_INSERT = 3
POSITION_TO_INSERT_AT_PARAMETER_FOR_INSERT = 4

NUMBER_OF_PARAMETERS_FOR_REMOVE_AT_POSITION = 1
NUMBER_OF_PARAMETERS_FOR_REMOVE_BETWEEN_TWO_POSITIONS = 3
NUMBER_OF_PARAMETERS_FOR_REMOVE_WITH_CONDITION = 2

POSITION_PARAMETER_FOR_REMOVE = 0
TO_KEYWORD_PARAMETER_FOR_REMOVE = 1
SECOND_POSITION_PARAMETER_FOR_REMOVE = 2

OLD_SCORE_PARAMETER_FOR_REPLACE = 0
PROBLEM_NUMBER_PARAMETER_FOR_REPLACE = 1
NEW_SCORE_PARAMETER_FOR_REPLACE = 2

NUMBER_OF_PARAMETERS_FOR_NORMAL_LIST = 0
NUMBER_OF_PARAMETERS_FOR_SORTED_LIST = 1
NUMBER_OF_PARAMETERS_FOR_LIST_WITH_CONDITION = 2

FIRST_PARAMETER_FOR_LIST = 0
SECOND_PARAMETER_FOR_LIST = 1

NUMBER_OF_PARAMETERS_FOR_TOP_BY_AVERAGE_SCORE = 1
NUMBER_OF_PARAMETERS_FOR_TOP_BY_PROBLEM_SCORE = 2

NUMBER_OF_CONTESTANTS_TO_DISPLAY_PARAMETER_FOR_TOP = 0
PROBLEM_NUMBER_PARAMETER_FOR_TOP = 1

SORT_BY_AVERAGE_SCORE = 0
SORT_BY_PROBLEM1 = 1
SORT_BY_PROBLEM2 = 2
SORT_BY_PROBLEM3 = 3

from texttable import Texttable

from src.contestant_scores import get_score_for_problem1, get_score_for_problem2, get_score_for_problem3
from src.functions import undo_last_operation, add_new_contestant_scores, \
    insert_new_contestant_scores, remove_average_scores_lower_than_given_value, \
    remove_average_scores_higher_than_given_value, remove_average_scores_equal_to_given_value, \
    remove_scores_at_certain_position, remove_scores_from_position1_to_position2, \
    replace_score_of_a_problem_for_a_contestant, list_average_scores_lower_than_given_value, \
    list_average_scores_equal_to_given_value, list_average_scores_higher_than_given_value, sort_contest_points_list


def display_contest_points_list(list_of_contest_points_to_print: list):
    contest_points_table = Texttable()
    contest_points_table.add_row(['', 'Problem 1', 'Problem 2', 'Problem 3'])
    for i in range(len(list_of_contest_points_to_print)):
        problem1_score = get_score_for_problem1(list_of_contest_points_to_print[i])
        problem2_score = get_score_for_problem2(list_of_contest_points_to_print[i])
        problem3_score = get_score_for_problem3(list_of_contest_points_to_print[i])
        contest_points_table.add_row([i + 1, problem1_score, problem2_score, problem3_score])
    print(contest_points_table.draw())


def ui_start(contest_points_list, contest_points_list_history):
    read_user_command(contest_points_list, contest_points_list_history)


def read_user_command(contest_points_list, contest_points_list_history):
    commands_list = {
        "add": function_add,
        "insert": function_insert,
        "remove": function_remove,
        "replace": function_replace,
        "undo": undo_last_operation
    }

    while True:
        try:
            command = input(">>> ")
            command = command.lower().split()
            first_command = command[FIRST_COMMAND]
            command.pop(FIRST_COMMAND)

            if first_command == "exit":
                break

            elif first_command == "list":
                list_to_display = function_list(command, contest_points_list)
                display_contest_points_list(list_to_display)

            elif first_command == "top":
                top_to_display = function_top(command, contest_points_list)
                display_contest_points_list(top_to_display)

            elif first_command in commands_list:
                commands_list[first_command](command, contest_points_list, contest_points_list_history)

            else:
                raise ValueError("ERROR: Command not found")

        except ValueError as error_message:
            print(error_message)


def function_add(remainder_of_command: list, contest_points_list: list, contest_points_list_history: list):
    if not len(remainder_of_command) == NUMBER_OF_PARAMETERS_FOR_ADD:
        raise ValueError("ERROR: Incorrect number of arguments provided for 'add'")

    try:
        score_for_problem1 = int(remainder_of_command[PROBLEM1_SCORE])
        score_for_problem2 = int(remainder_of_command[PROBLEM2_SCORE])
        score_for_problem3 = int(remainder_of_command[PROBLEM3_SCORE])
    except ValueError:
        raise ValueError("ERROR! Values must be integer only")

    add_new_contestant_scores(score_for_problem1, score_for_problem2, score_for_problem3, contest_points_list,
                              contest_points_list_history)


def function_insert(remainder_of_command: list, contest_points_list: list, contest_points_list_history: list):
    if not len(remainder_of_command) == NUMBER_OF_PARAMETERS_FOR_INSERT:
        raise ValueError("ERROR: Incorrect number of arguments provided for 'insert'")

    try:
        score_for_problem1 = int(remainder_of_command[PROBLEM1_SCORE])
        score_for_problem2 = int(remainder_of_command[PROBLEM2_SCORE])
        score_for_problem3 = int(remainder_of_command[PROBLEM3_SCORE])
    except ValueError:
        raise ValueError("ERROR: The values for the scores must be integers")

    if remainder_of_command[AT_KEYWORD_PARAMETER_FOR_INSERT] != "at":
        raise ValueError("ERROR: Command not found")

    try:
        position_to_insert_at = int(remainder_of_command[POSITION_TO_INSERT_AT_PARAMETER_FOR_INSERT])
    except ValueError:
        raise ValueError("ERROR: The position must be an integer")

    insert_new_contestant_scores(score_for_problem1, score_for_problem2, score_for_problem3, position_to_insert_at,
                                 contest_points_list, contest_points_list_history)


def function_remove(remainder_of_command: list, contest_points_list: list, contest_points_list_history: list):
    length_of_remainder_of_command = len(remainder_of_command)

    if length_of_remainder_of_command == NUMBER_OF_PARAMETERS_FOR_REMOVE_AT_POSITION:
        try:
            position_to_remove = int(remainder_of_command[POSITION_PARAMETER_FOR_REMOVE])
        except ValueError:
            raise ValueError("ERROR! The position value must be an integer")

        remove_scores_at_certain_position(contest_points_list, contest_points_list_history, position_to_remove)

    elif length_of_remainder_of_command == NUMBER_OF_PARAMETERS_FOR_REMOVE_BETWEEN_TWO_POSITIONS:
        try:
            first_position_to_remove = int(remainder_of_command[POSITION_PARAMETER_FOR_REMOVE]) - 1
        except ValueError:
            raise ValueError("ERROR! The position value must be an integer")

        if remainder_of_command[TO_KEYWORD_PARAMETER_FOR_REMOVE] != "to":
            raise ValueError("ERROR! Command not found")

        try:
            last_position_to_remove = int(remainder_of_command[SECOND_POSITION_PARAMETER_FOR_REMOVE]) - 1
        except ValueError:
            raise ValueError("ERROR! The position value must be an integer")

        remove_scores_from_position1_to_position2(contest_points_list, contest_points_list_history,
                                                  first_position_to_remove, last_position_to_remove)

    elif length_of_remainder_of_command == NUMBER_OF_PARAMETERS_FOR_REMOVE_WITH_CONDITION:
        operand_dictionary_remove = {
            "<": remove_average_scores_lower_than_given_value,
            ">": remove_average_scores_higher_than_given_value,
            "=": remove_average_scores_equal_to_given_value
        }

        if remainder_of_command[POSITION_PARAMETER_FOR_REMOVE] not in operand_dictionary_remove:
            raise ValueError("ERROR! Operand not recognised")
        else:
            try:
                value_to_compare_with = int(remainder_of_command[TO_KEYWORD_PARAMETER_FOR_REMOVE])
            except ValueError:
                raise ValueError("ERROR! The number to compare with must be an integer")

            contest_points_list_history.append(copy.deepcopy(contest_points_list))
            operand_dictionary_remove[remainder_of_command[POSITION_PARAMETER_FOR_REMOVE]](contest_points_list,
                                                                                           value_to_compare_with)

    else:
        raise ValueError("ERROR: Incorrect number of arguments provided for 'remove'")


def function_replace(remainder_of_command: list, contest_points_list: list, contest_points_list_history: list):
    try:
        contestant_number = int(remainder_of_command[OLD_SCORE_PARAMETER_FOR_REPLACE])
        new_score = int(remainder_of_command[NEW_SCORE_PARAMETER_FOR_REPLACE])
    except ValueError:
        raise ValueError("ERROR! Scores must be integers")

    problem_number = remainder_of_command[PROBLEM_NUMBER_PARAMETER_FOR_REPLACE]
    problem_number = problem_number.upper()

    replace_score_of_a_problem_for_a_contestant(contest_points_list[contestant_number - 1], contest_points_list,
                                                contest_points_list_history, problem_number, new_score)


def function_list(remainder_of_command: list, contest_points_list: list):
    length_of_remainder_of_command = len(remainder_of_command)
    if length_of_remainder_of_command == NUMBER_OF_PARAMETERS_FOR_NORMAL_LIST:
        return contest_points_list
    elif length_of_remainder_of_command == NUMBER_OF_PARAMETERS_FOR_SORTED_LIST:
        if remainder_of_command[FIRST_PARAMETER_FOR_LIST] == "sorted":
            sorted_contest_points_list = sort_contest_points_list(contest_points_list, SORT_BY_AVERAGE_SCORE)
            return sorted_contest_points_list
        else:
            raise ValueError("ERROR: Command not found")
    elif length_of_remainder_of_command == NUMBER_OF_PARAMETERS_FOR_LIST_WITH_CONDITION:
        operand_dictionary_list = {
            "<": list_average_scores_lower_than_given_value,
            ">": list_average_scores_higher_than_given_value,
            "=": list_average_scores_equal_to_given_value
        }
        if remainder_of_command[FIRST_PARAMETER_FOR_LIST] not in operand_dictionary_list:
            raise ValueError("ERROR! Operand not recognised")
        else:
            try:
                value_to_compare_with = int(remainder_of_command[SECOND_PARAMETER_FOR_LIST])
                return operand_dictionary_list[remainder_of_command[FIRST_PARAMETER_FOR_LIST]](contest_points_list,
                                                                                               value_to_compare_with)
            except ValueError:
                raise ValueError("ERROR! The number to compare with must be an integer")
    else:
        raise ValueError("ERROR: Incorrect number of arguments provided for 'add'")


def function_top(remainder_of_command: list, contest_points_list: list):
    if len(remainder_of_command) == NUMBER_OF_PARAMETERS_FOR_TOP_BY_AVERAGE_SCORE:
        try:
            numbers_of_positions = int(remainder_of_command[NUMBER_OF_CONTESTANTS_TO_DISPLAY_PARAMETER_FOR_TOP])
        except ValueError:
            raise ValueError("ERROR! The number of positions must be an integer")

        list_to_display = sort_contest_points_list(contest_points_list, SORT_BY_AVERAGE_SCORE)
        return list_to_display[:numbers_of_positions]

    elif len(remainder_of_command) == NUMBER_OF_PARAMETERS_FOR_TOP_BY_PROBLEM_SCORE:
        try:
            numbers_of_positions = int(remainder_of_command[NUMBER_OF_CONTESTANTS_TO_DISPLAY_PARAMETER_FOR_TOP])
        except ValueError:
            raise ValueError("ERROR! The number of positions must be an integer")

        if remainder_of_command[PROBLEM_NUMBER_PARAMETER_FOR_TOP].upper() == PROBLEM1:
            list_to_display = sort_contest_points_list(contest_points_list, SORT_BY_PROBLEM1)

        elif remainder_of_command[PROBLEM_NUMBER_PARAMETER_FOR_TOP].upper() == PROBLEM2:
            list_to_display = sort_contest_points_list(contest_points_list, SORT_BY_PROBLEM2)

        elif remainder_of_command[PROBLEM_NUMBER_PARAMETER_FOR_TOP].upper() == PROBLEM3:
            list_to_display = sort_contest_points_list(contest_points_list, SORT_BY_PROBLEM3)

        else:
            raise ValueError("ERROR! Problem number not found")

        return list_to_display[:numbers_of_positions]
    else:
        raise ValueError("ERROR! Incorrect number of arguments provided for 'top'")

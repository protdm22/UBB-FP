#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import copy
from random import randint

from src.contestant_scores import get_score_for_problem1, get_score_for_problem2, get_score_for_problem3, \
    return_contestant_scores, set_score_for_problem1, set_score_for_problem2, set_score_for_problem3

LOWEST_SCORE_ALLOWED = 0
HIGHEST_SCORE_ALLOWED = 10

PROBLEM1 = "P1"
PROBLEM2 = "P2"
PROBLEM3 = "P3"

SORT_BY_AVERAGE_SCORE = 0
SORT_BY_PROBLEM1 = 1
SORT_BY_PROBLEM2 = 2
SORT_BY_PROBLEM3 = 3


def generate_initial_scores() -> list:
    """
    Generates a list of 10 contestants with random scores for each problem
    :return: the list of 10 contestants
    """
    contestant_points_list = []
    for i in range(10):
        random_score_for_problem1 = randint(LOWEST_SCORE_ALLOWED, HIGHEST_SCORE_ALLOWED)
        random_score_for_problem2 = randint(LOWEST_SCORE_ALLOWED, HIGHEST_SCORE_ALLOWED)
        random_score_for_problem3 = randint(LOWEST_SCORE_ALLOWED, HIGHEST_SCORE_ALLOWED)
        contestant_points_list.append(
            return_contestant_scores(random_score_for_problem1, random_score_for_problem2, random_score_for_problem3))
    return contestant_points_list


def check_if_undo_available(history: list) -> bool:
    """
    Checks if the undo function is available
    :param history: a list that contains all the states for the contestant points list
    through the runtime of the program
    :return: True if undo can be done, False otherwise
    """
    if len(history) < 2:
        return False
    return True


def check_if_scores_between_0_and_10(score1, score2, score3) -> bool:
    """
    Checks if the scores for all problems are between 0 and 10
    :param score1: score for problem 1
    :param score2: score for problem 2
    :param score3: score for problem 3
    :return: True if score between 0 and 10, False otherwise
    """
    if LOWEST_SCORE_ALLOWED <= score1 <= HIGHEST_SCORE_ALLOWED and LOWEST_SCORE_ALLOWED <= score2 <= HIGHEST_SCORE_ALLOWED and LOWEST_SCORE_ALLOWED <= score3 <= HIGHEST_SCORE_ALLOWED:
        return True
    return False


def position_unavailable(position, contest_points_list) -> bool:
    """
    Checks if the given position exists in the list of points for all contestants
    :param position: the given position
    :param contest_points_list: the list of points for all contestants
    :return: True if it exists, False otherwise
    """
    if position > len(contest_points_list) or position < 0:
        return True
    return False


def get_contestant_average_score(contestant_scores) -> float:
    """
    Returns the average score of a contestant
    :param contestant_scores: a dictionary that contains the scores for all 3 problems
    :return: the average score
    """
    score_for_problem1 = get_score_for_problem1(contestant_scores)
    score_for_problem2 = get_score_for_problem2(contestant_scores)
    score_for_problem3 = get_score_for_problem3(contestant_scores)
    return (score_for_problem1 + score_for_problem2 + score_for_problem3) / 3


def sort_contest_points_list(contest_points_list: list, sort_criteria: int) -> list:
    """
    Sorts the list of points for all contestants in descending order by the sort criteria
    :param contest_points_list: the list of points for all contestants
    :param sort_criteria: the sort criteria
    :return: the sorted list
    """
    for i in range(len(contest_points_list) - 1):
        for j in range(i, len(contest_points_list)):

            if sort_criteria == SORT_BY_AVERAGE_SCORE:
                if get_contestant_average_score(contest_points_list[i]) < get_contestant_average_score(
                        contest_points_list[j]):
                    contest_points_list[i], contest_points_list[j] = contest_points_list[j], contest_points_list[i]

            elif sort_criteria == SORT_BY_PROBLEM1:
                if get_score_for_problem1(contest_points_list[i]) < get_score_for_problem1(
                        contest_points_list[j]):
                    contest_points_list[i], contest_points_list[j] = contest_points_list[j], contest_points_list[i]

            elif sort_criteria == SORT_BY_PROBLEM2:
                if get_score_for_problem2(contest_points_list[i]) < get_score_for_problem2(
                        contest_points_list[j]):
                    contest_points_list[i], contest_points_list[j] = contest_points_list[j], contest_points_list[i]

            elif sort_criteria == SORT_BY_PROBLEM3:
                if get_score_for_problem3(contest_points_list[i]) < get_score_for_problem3(
                        contest_points_list[j]):
                    contest_points_list[i], contest_points_list[j] = contest_points_list[j], contest_points_list[i]

    return contest_points_list


# (A) add
def add_new_contestant_scores(score_for_problem1, score_for_problem2, score_for_problem3, contest_points_list: list,
                              contest_points_list_history: list):
    """
    Appends the scores of a new contestant to the list of points for all contestants
    :param score_for_problem1: score for problem 1
    :param score_for_problem2: score for problem 2
    :param score_for_problem3: score for problem 3
    :param contest_points_list: list of points for all contestants
    :param contest_points_list_history: history of the list of points for all contestants (for undo)
    :return: None
    """
    if not check_if_scores_between_0_and_10(score_for_problem1, score_for_problem2, score_for_problem3):
        raise ValueError("ERROR: Scores must be between 0 and 10")
    contest_points_list_history.append(contest_points_list.copy())
    contest_points_list.append(
        return_contestant_scores(score_for_problem1, score_for_problem2, score_for_problem3))


# (A) insert
def insert_new_contestant_scores(score_for_problem1, score_for_problem2, score_for_problem3, position_to_insert_at,
                                 contest_points_list, contest_points_list_history):
    """
    Inserts the scores of a new contestant to the list of points for all contestants at a given position
    :param score_for_problem1: score for problem 1
    :param score_for_problem2: score for problem 2
    :param score_for_problem3: score for problem 3
    :param position_to_insert_at: the given position
    :param contest_points_list: list of points for all contestants
    :param contest_points_list_history: history of the list of points for all contestants (for undo)
    :return: None
    """
    if not check_if_scores_between_0_and_10(score_for_problem1, score_for_problem2, score_for_problem3):
        raise ValueError("ERROR: Scores must be between 0 and 10")
    if position_unavailable(position_to_insert_at, contest_points_list):
        raise ValueError(f"ERROR: There aren't enough entries to insert at position {position_to_insert_at}")
    contest_points_list_history.append(contest_points_list.copy())
    contest_points_list.insert(position_to_insert_at - 1,
                               return_contestant_scores(score_for_problem1, score_for_problem2, score_for_problem3))


# (B) remove
def set_scores_to_0(contestant_scores):
    """
    Sets the scores of all problems of a contestant to 0
    :param contestant_scores: the scores of the contestant
    :return: None
    """
    set_score_for_problem1(contestant_scores, 0)
    set_score_for_problem2(contestant_scores, 0)
    set_score_for_problem3(contestant_scores, 0)


def remove_scores_at_certain_position(contest_points_list, contest_points_list_history, position_to_remove):
    """
    Sets the scores to 0 at the given position
    :param contest_points_list: list of points for all contestants
    :param contest_points_list_history: history of the list of points for all contestants (for undo)
    :param position_to_remove: the given position
    :return: None
    """
    if position_unavailable(position_to_remove, contest_points_list):
        raise ValueError(f"ERROR! No contestants found on position {position_to_remove}")
    contest_points_list_history.append(copy.deepcopy(contest_points_list))
    set_scores_to_0(contest_points_list[position_to_remove - 1])


def remove_scores_from_position1_to_position2(contest_points_list, contest_points_list_history, position1, position2):
    """
    Sets all scores to 0 between the first and second given positions
    :param contest_points_list: list of points for all contestants
    :param contest_points_list_history: history of the list of points for all contestants (for undo)
    :param position1: the first given position
    :param position2: the second given position
    :return: None
    """
    if position_unavailable(position1, contest_points_list):
        raise ValueError("ERROR! The first position is out of bounds")
    if position_unavailable(position2, contest_points_list):
        raise ValueError("ERROR! The last position is out of bounds")
    contest_points_list_history.append(copy.deepcopy(contest_points_list))
    for i in range(position1, position2 + 1):
        set_scores_to_0(contest_points_list[i])


# (D) remove
def remove_average_scores_lower_than_given_value(contest_points_list: list, given_value):
    """
    Sets all scores to 0 where the average score is lower than the given value
    :param contest_points_list: list of points for all contestants
    :param given_value: the given value
    :return: None
    """
    for i in range(len(contest_points_list)):
        if get_contestant_average_score(contest_points_list[i]) < given_value / 10:
            set_scores_to_0(contest_points_list[i])


def remove_average_scores_higher_than_given_value(contest_points_list: list, given_value):
    """
    Sets all scores to 0 where the average score is higher than the given value
    :param contest_points_list: list of points for all contestants
    :param given_value: the given value
    :return: None
    """
    for i in range(len(contest_points_list)):
        if get_contestant_average_score(contest_points_list[i]) > given_value / 10:
            set_scores_to_0(contest_points_list[i])


def remove_average_scores_equal_to_given_value(contest_points_list: list, given_value):
    """
    Sets all scores to 0 where the average score is equal to the given value
    :param contest_points_list: list of points for all contestants
    :param given_value: the given value
    :return: None
    """
    for i in range(len(contest_points_list)):
        if get_contestant_average_score(contest_points_list[i]) == given_value / 10:
            set_scores_to_0(contest_points_list[i])


# (B) replace
def replace_score_of_a_problem_for_a_contestant(contestant, contest_points_list, contest_points_list_history,
                                                problem_number, new_score):
    """
    Replaces the value of the specified problem from the given contestant with a new value
    :param contestant: the given contestant
    :param contest_points_list: list of points for all contestants
    :param contest_points_list_history: history of the list of points for all contestants (for undo)
    :param problem_number: the specified problem
    :param new_score: the new value
    :return: None
    """
    contest_points_list_history.append(copy.deepcopy(contest_points_list))

    if problem_number not in (PROBLEM1, PROBLEM2, PROBLEM3):
        raise ValueError("ERROR! Problem not recognised")

    if not LOWEST_SCORE_ALLOWED <= new_score <= HIGHEST_SCORE_ALLOWED:
        raise ValueError("ERROR: New score must be between 0 and 10")

    if problem_number == PROBLEM1:
        set_score_for_problem1(contestant, new_score)
    if problem_number == PROBLEM2:
        set_score_for_problem2(contestant, new_score)
    if problem_number == PROBLEM3:
        set_score_for_problem3(contestant, new_score)


# (C) list
def list_average_scores_lower_than_given_value(contest_points_list: list, given_value: int) -> list:
    """
    Returns a list where only the contestants that have their average score lower than the given value are appended
    :param contest_points_list: list of points for all contestants
    :param given_value: the given value
    :return: the requested list
    """
    list_to_print = []
    for i in range(len(contest_points_list)):
        if get_contestant_average_score(contest_points_list[i]) < given_value:
            list_to_print.append(contest_points_list[i])
    return list_to_print


def list_average_scores_higher_than_given_value(contest_points_list, given_value):
    """
    Returns a list where only the contestants that have their average score higher than the given value are appended
    :param contest_points_list: list of points for all contestants
    :param given_value: the given value
    :return: the requested list
    """
    list_to_print = []
    for i in range(len(contest_points_list)):
        if get_contestant_average_score(contest_points_list[i]) > given_value:
            list_to_print.append(contest_points_list[i])
    return list_to_print


def list_average_scores_equal_to_given_value(contest_points_list, given_value):
    """
    Returns a list where only the contestants that have their average score equal to the given value are appended
    :param contest_points_list: list of points for all contestants
    :param given_value: the given value
    :return: the requested list
    """
    list_to_print = []
    for i in range(len(contest_points_list)):
        if get_contestant_average_score(contest_points_list[i]) == given_value:
            list_to_print.append(contest_points_list[i])
    return list_to_print


# (E) undo
def undo_last_operation(remainder_of_command: list, contest_points_list: list, contest_points_list_history: list):
    """
    Undoes the last operation done
    :param remainder_of_command: unused parameter
    :param contest_points_list: list of points for all contestants
    :param contest_points_list_history: history of the list of points for all contestants (for undo)
    :return: None
    """
    if check_if_undo_available(contest_points_list_history):
        last_state = contest_points_list_history.pop().copy()
        contest_points_list.clear()
        contest_points_list.extend(last_state)
    else:
        raise ValueError("ERROR! Undo unavailable")

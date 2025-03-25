from src.functions import add_new_contestant_scores, insert_new_contestant_scores, remove_scores_at_certain_position, \
    remove_scores_from_position1_to_position2, replace_score_of_a_problem_for_a_contestant


def test_add_new_contestant_scores():
    contest_points_list = []
    contest_points_list_history = []

    # Test adding valid scores
    add_new_contestant_scores(5, 6, 7, contest_points_list, contest_points_list_history)
    assert contest_points_list == [
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7}], "Adding valid scores failed"
    assert contest_points_list_history == [[]], "History not updated correctly"

    # Test adding invalid scores
    try:
        add_new_contestant_scores(11, 6, 7, contest_points_list, contest_points_list_history)
        assert False, "Test for add failed. Score outside of bounds"
    except ValueError:
        assert True  # Correct error raised for score outside of bounds


def test_insert_new_contestant_scores():
    contest_points_list = [{"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7}]
    contest_points_list_history = []

    # Test inserting at a valid position
    insert_new_contestant_scores(8, 9, 10, 1, contest_points_list, contest_points_list_history)
    assert contest_points_list == [
        {"score_for_problem1": 8, "score_for_problem2": 9, "score_for_problem3": 10},
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7}
    ], "Inserting valid scores at a valid position failed"
    assert contest_points_list_history == [[
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7}
    ]], "History not updated correctly"

    # Test inserting at an invalid position
    try:
        insert_new_contestant_scores(3, 4, 5, 5, contest_points_list, contest_points_list_history)
        assert False, "Test for insert failed. Position out of range"
    except ValueError:
        assert True  # Correct error raised for position out of range


def test_remove_scores_at_certain_position():
    contest_points_list = [
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7},
        {"score_for_problem1": 8, "score_for_problem2": 9, "score_for_problem3": 10}
    ]
    contest_points_list_history = []

    # Test valid position
    remove_scores_at_certain_position(contest_points_list, contest_points_list_history, 1)
    assert contest_points_list == [
        {"score_for_problem1": 0, "score_for_problem2": 0, "score_for_problem3": 0},
        {"score_for_problem1": 8, "score_for_problem2": 9, "score_for_problem3": 10}
    ], "Failed removing scores at position 1"
    assert contest_points_list_history == [[
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7},
        {"score_for_problem1": 8, "score_for_problem2": 9, "score_for_problem3": 10}
    ]], "History not updated correctly"

    # Test invalid position
    try:
        remove_scores_at_certain_position(contest_points_list, contest_points_list_history, 5)
        assert False, "Test for remove failed. Position out of range"
    except ValueError:
        assert True  # Correct error raised for position out of range


def test_remove_scores_from_position1_to_position2():
    contest_points_list = [
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7},
        {"score_for_problem1": 8, "score_for_problem2": 9, "score_for_problem3": 10},
        {"score_for_problem1": 3, "score_for_problem2": 4, "score_for_problem3": 5}
    ]
    contest_points_list_history = []

    # Test valid removal range
    remove_scores_from_position1_to_position2(contest_points_list, contest_points_list_history, 0, 1)
    assert contest_points_list == [
        {"score_for_problem1": 0, "score_for_problem2": 0, "score_for_problem3": 0},
        {"score_for_problem1": 0, "score_for_problem2": 0, "score_for_problem3": 0},
        {"score_for_problem1": 3, "score_for_problem2": 4, "score_for_problem3": 5}
    ], "Failed removing scores in valid range"
    assert contest_points_list_history == [[
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7},
        {"score_for_problem1": 8, "score_for_problem2": 9, "score_for_problem3": 10},
        {"score_for_problem1": 3, "score_for_problem2": 4, "score_for_problem3": 5}
    ]], "History not updated correctly"

    # Test invalid range
    try:
        remove_scores_from_position1_to_position2(contest_points_list, contest_points_list_history, -1, 2)
        assert False, "Test for remove failed. Position1 is out of range"
    except ValueError:
        assert True  # Correct error raised for position1 out of range

    try:
        remove_scores_from_position1_to_position2(contest_points_list, contest_points_list_history, 1, 10)
        assert False, "Test for remove failed. Position1 is out of range"
    except ValueError:
        assert True  # Correct error raised for position1 out of range


def test_replace_score_of_a_problem_for_a_contestant():
    contest_points_list = [
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7}
    ]
    contest_points_list_history = []

    # Test valid replacement
    replace_score_of_a_problem_for_a_contestant(
        contest_points_list[0], contest_points_list, contest_points_list_history, "P1", 10
    )
    assert contest_points_list == [
        {"score_for_problem1": 10, "score_for_problem2": 6, "score_for_problem3": 7}
    ], "Failed replacing problem 1 with score 10"
    assert contest_points_list_history == [[
        {"score_for_problem1": 5, "score_for_problem2": 6, "score_for_problem3": 7}
    ]], "History not updated correctly"

    # Test invalid problem numbers
    try:
        replace_score_of_a_problem_for_a_contestant(
            contest_points_list[0], contest_points_list, contest_points_list_history, 4, 10
        )
        assert False, "Test for replace failed. Invalid problem number"
    except ValueError:
        assert True  # Correct error raised for invalid problem number

    # Test invalid new score
    try:
        replace_score_of_a_problem_for_a_contestant(
            contest_points_list[0], contest_points_list, contest_points_list_history, 1, -5
        )
        assert False, "Test for replace failed. Score out of bounds"
    except ValueError:
        assert True  # Correct error raised by score out of bounds


if __name__ == "__main__":
    test_add_new_contestant_scores()
    test_insert_new_contestant_scores()
    test_remove_scores_at_certain_position()
    test_remove_scores_from_position1_to_position2()
    test_replace_score_of_a_problem_for_a_contestant()

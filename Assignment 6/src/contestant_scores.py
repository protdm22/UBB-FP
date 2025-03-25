def return_contestant_scores(score_for_problem1: int, score_for_problem2: int, score_for_problem3: int):
    return {"score_for_problem1": score_for_problem1, "score_for_problem2": score_for_problem2,
            "score_for_problem3": score_for_problem3}


def get_score_for_problem1(contestant_scores):
    return contestant_scores["score_for_problem1"]


def get_score_for_problem2(contestant_scores):
    return contestant_scores["score_for_problem2"]


def get_score_for_problem3(contestant_scores):
    return contestant_scores["score_for_problem3"]


def set_score_for_problem1(contestant_scores, new_score_for_problem1):
    contestant_scores["score_for_problem1"] = new_score_for_problem1


def set_score_for_problem2(contestant_scores, new_score_for_problem2):
    contestant_scores["score_for_problem2"] = new_score_for_problem2


def set_score_for_problem3(contestant_scores, new_score_for_problem3):
    contestant_scores["score_for_problem3"] = new_score_for_problem3

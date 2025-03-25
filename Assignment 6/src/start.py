#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
from src.functions import generate_initial_scores
from src.ui import ui_start

if __name__ == "__main__":
    contest_points_list = generate_initial_scores()
    contest_points_list_history = [contest_points_list.copy()]
    ui_start(contest_points_list,contest_points_list_history)

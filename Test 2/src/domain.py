class Assignment:
    def __init__(self, assignment_id, student_name, assignment_solution):
        self.__id = assignment_id
        self.__student_name = student_name
        self.__solution = assignment_solution

    @property
    def id(self):
        return self.__id

    @property
    def student_name(self):
        return self.__student_name

    @property
    def solution(self):
        return self.__solution

    def set_student_name(self, new_student_name):
        self.__student_name = new_student_name

    def set_assignment_solution(self, new_solution):
        self.__solution = new_solution

    def __str__(self):
        return f"{self.__student_name}'s assignment (ID={self.__id}) solution is: {self.__solution}"

import json

from src.domain.domain_object import DomainObject

MINIMUM_GRADE = 0


class Grade(DomainObject):
    def __init__(self, grade_id: str = "", student_id: str = "", discipline_id: str = "",
                 grade_value: float = MINIMUM_GRADE):
        self.__grade_id = grade_id
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = grade_value

    @property
    def id(self):
        return self.__grade_id

    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def value(self):
        return self.__grade_value

    def set_grade_value(self, new_grade_value):
        self.__grade_value = new_grade_value

    def __str__(self):
        return f"Grade {int(self.__grade_value) if self.__grade_value.is_integer() else self.__grade_value}"

    def __eq__(self, other):
        return self.__student_id == other.student_id and self.__discipline_id == other.discipline_id

    def write_to_json(self):
        grade = \
            {
                "grade_id": self.__grade_id,
                "student_id": self.__student_id,
                "discipline_id": self.__discipline_id,
                "grade_value": self.__grade_value
            }
        return json.dumps(grade)

    def read_from_json(self, grade_json):
        json_data = json.loads(grade_json)
        self.__grade_id = json_data["grade_id"]
        self.__student_id = json_data["student_id"]
        self.__discipline_id = json_data["discipline_id"]
        self.__grade_value = json_data["grade_value"]

import json

from src.domain.domain_object import DomainObject


class Student(DomainObject):
    def __init__(self, student_name: str = "", student_id: str = ""):
        self.__id = student_id
        self.__name = student_name

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return "Student"

    def set_name(self, new_name):
        self.__name = new_name

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return f"Student with ID={self.__id} has the name '{self.__name}'"

    def write_to_json(self):
        student = \
            {
                "id": self.__id,
                "name": self.__name
            }
        return json.dumps(student)

    def read_from_json(self, student_json):
        json_data = json.loads(student_json)
        self.__id = json_data["id"]
        self.__name = json_data["name"]

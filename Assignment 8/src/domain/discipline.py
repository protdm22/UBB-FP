import json

from src.domain.domain_object import DomainObject


class Discipline(DomainObject):
    def __init__(self, discipline_name: str = "", discipline_id: str = ""):
        self.__name = discipline_name
        self.__id = discipline_id

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return "Discipline"

    def set_name(self, new_name):
        self.__name = new_name

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return f"Discipline with ID={self.__id} has the name '{self.__name}'"

    def write_to_json(self):
        discipline = \
            {
                "id": self.__id,
                "name": self.__name
            }
        return json.dumps(discipline)

    def read_from_json(self, discipline_json):
        json_data = json.loads(discipline_json)
        self.__id = json_data["id"]
        self.__name = json_data["name"]
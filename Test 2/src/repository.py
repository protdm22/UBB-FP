from src.domain import Assignment

ASSIGNMENT_ID = 0
STUDENT_NAME = 1
ASSIGNMENT_SOLUTION = 2


class ObjectAlreadyExistsException(Exception):
    pass


class ObjectNotFoundException(Exception):
    pass


class Repository:
    def __init__(self, filename):
        self.__data = {}
        self.__filename = filename
        self.__load_data()

    def add_entry(self, new_object):
        """
        Adds a new object to the repository
        :param new_object: the added object
        :return: None
        """
        if new_object.id in self.__data:
            raise ObjectAlreadyExistsException
        self.__data[new_object.id] = new_object
        self.__save_data()

    def remove_entry(self, object_id):
        if not object_id in self.__data:
            raise ObjectNotFoundException
        del self.__data[object_id]
        self.__save_data()

    def update_entry(self, object_id, new_object):
        if not object_id in self.__data:
            raise ObjectNotFoundException
        self.__data[object_id] = new_object
        self.__save_data()

    def find_entry_by_id(self, object_id):
        return self.__data.get(object_id)

    def get_all_entries(self):
        return [*self.__data.values()]

    def __load_data(self):
        input_file = open(self.__filename, "rt")
        all_lines = input_file.readlines()
        input_file.close()
        for line in all_lines:
            line = line.strip()
            line = line.split(',')
            assignment_id = int(line[ASSIGNMENT_ID])
            student_name = line[STUDENT_NAME].strip()
            assignment_solution = line[ASSIGNMENT_SOLUTION].strip()
            new_assignment = Assignment(assignment_id, student_name, assignment_solution)
            self.__data[assignment_id] = new_assignment

    def __save_data(self):
        output_file = open(self.__filename, "wt")
        for assignment in self.get_all_entries():
            output_file.write(f"{assignment.id}, {assignment.student_name}, {assignment.solution}\n")
        output_file.close()

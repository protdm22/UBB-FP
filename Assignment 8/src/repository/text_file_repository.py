import os.path

from src.repository.memory_repository import MemoryRepository


class TextFileRepository(MemoryRepository):
    def __init__(self, filename, repository_type):
        super().__init__(filename, repository_type)
        self.__filename = filename
        if os.path.exists(self.__filename):
            self.__load_data()
        else:
            self.__save_data()

    def add_entry(self, new_object):
        super().add_entry(new_object)
        self.__save_data()

    def remove_entry(self, object_id):
        super().remove_entry(object_id)
        self.__save_data()

    def update_entry(self, object_id, new_object_name):
        super().update_entry(object_id, new_object_name)
        self.__save_data()

    def __save_data(self):
        output_file = open(self.__filename, "wt")
        for object in self.get_all_entries():
            output_file.write(object.write_to_json() + '\n')
        output_file.close()

    def __load_data(self):
        input_file = open(self.__filename, "rt")
        lines = input_file.readlines()
        input_file.close()
        for line in lines:
            line = line.strip()
            new_object = self._repository_type()
            new_object.read_from_json(line)
            super().add_entry(new_object)

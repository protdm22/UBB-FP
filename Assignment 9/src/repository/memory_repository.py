from src.domain.domain_object import DomainObject
from src.repository.repository import Repository
from src.repository.repository_exceptions import ObjectAlreadyExistsException, ObjectNotFoundException


class MemoryRepository(Repository):
    def __init__(self, _filename, repository_type):
        self._data = {}
        self._repository_type = repository_type

    def add_entry(self, new_object):
        if new_object.id in self._data:
            raise ObjectAlreadyExistsException(
                f"An object of type '{new_object.type}' with ID={new_object.id} already exists")
        self._data[new_object.id] = new_object

    def remove_entry(self, object_id):
        if object_id not in self._data:
            raise ObjectNotFoundException(f"No objects with ID={object_id} found")
        del self._data[object_id]

    def update_entry(self, object_id, new_object_name):
        if not self.find_entry_by_id(object_id):
            raise ObjectNotFoundException(f"No objects with ID={object_id} found")
        changed_object = self.find_entry_by_id(object_id)
        changed_object.set_name(new_object_name)
        self._data[object_id] = changed_object

    def get_all_entries(self):
        return [*self._data.values()]

    def find_entry_by_id(self, object_id):
        return self._data.get(object_id)

    def __len__(self):
        return len(self.get_all_entries())

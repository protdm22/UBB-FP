from src.domain.discipline import Discipline
from src.repository.repository import Repository
from src.services.service_exceptions import NoMatchingSearches
from src.services.undo_redo_service import FunctionCall, Operation, CascadedOperation
from src.utilities.generator_utilities import GeneratorUtilities

NO_ELEMENTS = 0

NUMBER_OF_DISCIPLINES_TO_GENERATE = 20


class DisciplineService:
    def __init__(self, discipline_repository: Repository, grade_repository: Repository, undo_redo_service):
        self.__discipline_repository = discipline_repository
        self.__grade_repository = grade_repository
        self.__undo_redo_service = undo_redo_service

        if len(self.__discipline_repository) == NO_ELEMENTS:
            list_of_random_disciplines = GeneratorUtilities.generate_random_disciplines(
                NUMBER_OF_DISCIPLINES_TO_GENERATE)
            for discipline in list_of_random_disciplines:
                new_discipline = Discipline(discipline.name, discipline.id)
                self.__discipline_repository.add_entry(new_discipline)

    def add_discipline(self, new_discipline_name, new_discipline_id):
        """
        Adds a new Discipline entry in the repository
        :param new_discipline_name: the name of the new discipline
        :param new_discipline_id: the ID of the new discipline
        :return: None
        """
        new_discipline = Discipline(new_discipline_name, new_discipline_id)
        self.__discipline_repository.add_entry(new_discipline)

        redo_add_discipline_function = FunctionCall(self.__discipline_repository.add_entry, new_discipline)
        undo_add_discipline_function = FunctionCall(self.__discipline_repository.remove_entry, new_discipline_id)
        self.__undo_redo_service.record_undo(Operation(undo_add_discipline_function, redo_add_discipline_function))

    def remove_discipline(self, discipline_id):
        """
        Removes the discipline with the given id from the repository
        :param discipline_id: the ID of the discipline
        :return: None
        """
        redo_remove_discipline_function = FunctionCall(self.__discipline_repository.remove_entry, discipline_id)
        undo_remove_discipline_function = FunctionCall(self.__discipline_repository.add_entry,
                                                       self.__discipline_repository.find_entry_by_id(discipline_id))
        undo_redo_operations = [Operation(undo_remove_discipline_function, redo_remove_discipline_function)]

        self.__discipline_repository.remove_entry(discipline_id)

        list_of_all_grades = self.__grade_repository.get_all_entries()
        for grade in list_of_all_grades:
            if grade.discipline_id == discipline_id:
                redo_remove_discipline_grade_function = FunctionCall(self.__grade_repository.remove_entry, grade.id)
                undo_remove_discipline_grade_function = FunctionCall(self.__grade_repository.add_entry, grade)
                undo_redo_operations.append(
                    Operation(undo_remove_discipline_grade_function, redo_remove_discipline_grade_function))

                self.__grade_repository.remove_entry(grade.id)

        self.__undo_redo_service.record_undo(CascadedOperation(*undo_redo_operations))

    def update_discipline(self, discipline_id, new_discipline_name):
        """
        Updates the name of a discipline with a given ID in the repository
        :param discipline_id: the ID of the discipline
        :param new_discipline_name: the new name of the discipline
        :return:
        """
        redo_update_discipline_function = FunctionCall(self.__discipline_repository.update_entry, discipline_id,
                                                       new_discipline_name)
        undo_update_discipline_function = FunctionCall(self.__discipline_repository.update_entry, discipline_id,
                                                       self.__discipline_repository.find_entry_by_id(
                                                           discipline_id).name)
        self.__undo_redo_service.record_undo(
            Operation(undo_update_discipline_function, redo_update_discipline_function))

        self.__discipline_repository.update_entry(discipline_id, new_discipline_name)

    def return_all_disciplines(self):
        """
        Returns a list of all the disciplines from the repository
        :return: the list of all disciplines
        """
        return self.__discipline_repository.get_all_entries()

    def search_for_disciplines(self, discipline_to_search):
        list_of_matching_disciplines = []
        list_of_all_disciplines = self.__discipline_repository.get_all_entries()

        for discipline in list_of_all_disciplines:
            if discipline_to_search in discipline.id:
                list_of_matching_disciplines.append(discipline)

        if len(list_of_matching_disciplines) != NO_ELEMENTS:
            return list_of_matching_disciplines

        for discipline in list_of_all_disciplines:
            if discipline_to_search.lower() in discipline.name.lower():
                list_of_matching_disciplines.append(discipline)

        if len(list_of_matching_disciplines) != NO_ELEMENTS:
            return list_of_matching_disciplines
        else:
            raise NoMatchingSearches("No matching disciplines found")

    def return_discipline_by_id(self, discipline_id):
        return self.__discipline_repository.find_entry_by_id(discipline_id)

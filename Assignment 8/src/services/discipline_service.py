from src.domain.discipline import Discipline
from src.repository.repository import Repository
from src.services.service_exceptions import NoMatchingSearches
from src.utilities.generator_utilities import GeneratorUtilities

NO_ELEMENTS = 0


class DisciplineService:
    def __init__(self, discipline_repository: Repository, grade_repository: Repository):
        self.__discipline_repository = discipline_repository
        self.__grade_repository = grade_repository

        if len(self.__discipline_repository) == NO_ELEMENTS:
            list_of_random_disciplines = GeneratorUtilities.generate_random_disciplines(20)
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

    def remove_discipline(self, discipline_id):
        """
        Removes the discipline with the given id from the repository
        :param discipline_id: the ID of the discipline
        :return: None
        """
        self.__discipline_repository.remove_entry(discipline_id)

        list_of_all_grades = self.__grade_repository.get_all_entries()
        for grade in list_of_all_grades:
            if grade.discipline_id == discipline_id:
                self.__grade_repository.remove_entry(grade.id)

    def update_discipline(self, discipline_id, new_discipline_name):
        """
        Updates the name of a discipline with a given ID in the repository
        :param discipline_id: the ID of the discipline
        :param new_discipline_name: the new name of the discipline
        :return:
        """
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

    def return_discipline_by_id(self,discipline_id):
        return self.__discipline_repository.find_entry_by_id(discipline_id)

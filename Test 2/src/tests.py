import unittest

from src.domain import Assignment
from src.repository import Repository, STUDENT_NAME
from src.services import Services


class Tests(unittest.TestCase):
    def test_add_student(self):
        repository = Repository("repository.txt")
        new_assignment = Assignment(10, "Martin", "This is my solution")
        repository.add_entry(new_assignment)
        self.assertEqual(repository.find_entry_by_id(10), new_assignment)
        service = Services(repository)
        try:
            service.add_assignment("Martin", "This is my solution")
        except Exception:
            self.fail()


if __name__ == "__main__":
    unittest.main()

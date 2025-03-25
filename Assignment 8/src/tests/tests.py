import unittest

from src.domain.discipline import Discipline
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.memory_repository import MemoryRepository
from src.services.discipline_service import DisciplineService
from src.services.student_service import StudentService


class Tests(unittest.TestCase):
    # tests for students
    def test_add_student(self):
        student_repository = MemoryRepository("", Student)
        grade_repository = MemoryRepository("", Grade)

        student_id = "30"
        student_name = "John Smith"
        student_service = StudentService(student_repository, grade_repository)

        student_service.add_student(student_name, student_id)

        verification_student = student_service.return_student_by_id(student_id)

        self.assertEqual(verification_student.id, "30")
        self.assertEqual(verification_student.name, "John Smith")

    def test_remove_student(self):
        student_repository = MemoryRepository("", Student)
        grade_repository = MemoryRepository("", Grade)

        student_service = StudentService(student_repository, grade_repository)
        student_service.add_student("John Smith", "30")

        student_service.remove_student("30")

        self.assertEqual(student_repository.find_entry_by_id("30"), None)

    def test_update_student(self):
        student_repository = MemoryRepository("", Student)
        grade_repository = MemoryRepository("", Grade)

        student_service = StudentService(student_repository, grade_repository)
        student_service.add_student("John Smith", "30")

        updated_student_name = "Jake Doe"
        student_service.update_student("30", updated_student_name)

        verification_student = student_service.return_student_by_id("30")

        self.assertEqual(verification_student.id, "30")
        self.assertEqual(verification_student.name, "Jake Doe")

    # tests for disciplines
    def test_add_discipline(self):
        discipline_repository = MemoryRepository("", Discipline)
        grade_repository = MemoryRepository("", Grade)

        discipline_id = "30"
        discipline_name = "John Smith"
        discipline_service = DisciplineService(discipline_repository, grade_repository)

        discipline_service.add_discipline(discipline_name, discipline_id)

        verification_discipline = discipline_service.return_discipline_by_id(discipline_id)

        self.assertEqual(verification_discipline.id, "30")
        self.assertEqual(verification_discipline.name, "John Smith")

    def test_remove_discipline(self):
        discipline_repository = MemoryRepository("", Discipline)
        grade_repository = MemoryRepository("", Grade)

        discipline_service = DisciplineService(discipline_repository, grade_repository)
        discipline_service.add_discipline("John Smith", "30")

        discipline_service.remove_discipline("30")

        self.assertEqual(discipline_repository.find_entry_by_id("30"), None)

    def test_update_discipline(self):
        discipline_repository = MemoryRepository("", Discipline)
        grade_repository = MemoryRepository("", Grade)

        discipline_service = DisciplineService(discipline_repository, grade_repository)
        discipline_service.add_discipline("John Smith", "30")

        updated_discipline_name = "Jake Doe"
        discipline_service.update_discipline("30", updated_discipline_name)

        verification_discipline = discipline_service.return_discipline_by_id("30")

        self.assertEqual(verification_discipline.id, "30")
        self.assertEqual(verification_discipline.name, "Jake Doe")


if __name__ == "__main__":
    unittest.main()

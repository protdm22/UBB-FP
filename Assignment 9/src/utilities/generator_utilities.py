from faker import Faker
import random
from src.domain.discipline import Discipline
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.repository import Repository

MINIMUM_GRADE = 0
MAXIMUM_GRADE = 10

TWO_DECIMALS = 2


class GeneratorUtilities:
    @staticmethod
    def generate_random_students(number_of_students_to_generate):
        fake = Faker()
        list_of_random_students = []

        for i in range(number_of_students_to_generate):
            random_student_name = fake.name()
            student_id = str(i + 1)
            new_random_student = Student(random_student_name, student_id)
            list_of_random_students.append(new_random_student)

        return list_of_random_students

    @staticmethod
    def generate_random_disciplines(number_of_disciplines_to_generate):
        predefined_disciplines = [
            "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
            "History", "Geography", "Economics", "Philosophy", "Literature",
            "Art", "Music", "Physical Education", "Psychology", "Sociology",
            "Astronomy", "Engineering", "Statistics", "Political Science", "Environmental Science",
            "Introduction to Programming", "Object-Oriented Programming",
            "Data Structures", "Algorithms", "Computer Architecture",
            "Operating Systems", "Databases", "Computer Networks",
            "Software Engineering", "Web Development Basics",
            "Calculus", "Linear Algebra"
        ]

        list_of_random_disciplines = []

        for i in range(number_of_disciplines_to_generate):
            random_discipline_name = random.choice(predefined_disciplines)
            predefined_disciplines.remove(random_discipline_name)
            discipline_id = str(i + 1)
            new_random_discipline = Discipline(random_discipline_name, discipline_id)
            list_of_random_disciplines.append(new_random_discipline)

        return list_of_random_disciplines

    @staticmethod
    def generate_random_grades(number_of_grades_to_generate, student_repository: Repository,
                               discipline_repository: Repository):
        list_of_random_grades = []

        list_of_student_ids = []
        list_of_discipline_ids = []

        list_of_students = student_repository.get_all_entries()
        list_of_disciplines = discipline_repository.get_all_entries()

        for student in list_of_students:
            list_of_student_ids.append(student.id)

        for discipline in list_of_disciplines:
            list_of_discipline_ids.append(discipline.id)

        for i in range(number_of_grades_to_generate):
            grade_id = str(i + 1)
            random_student_id = str(random.choice(list_of_student_ids))
            random_discipline_id = str(random.choice(list_of_discipline_ids))
            random_grade_value = round(random.uniform(MINIMUM_GRADE, MAXIMUM_GRADE), TWO_DECIMALS)

            random_bonus_1 = random.uniform(MINIMUM_GRADE, MAXIMUM_GRADE - random_grade_value)
            random_grade_value += random_bonus_1

            random_bonus_2 = random.uniform(MINIMUM_GRADE, MAXIMUM_GRADE - random_grade_value)
            random_grade_value += random_bonus_2

            random_grade_value = round(random_grade_value, TWO_DECIMALS)

            new_grade = Grade(grade_id, random_student_id, random_discipline_id, random_grade_value)
            list_of_random_grades.append(new_grade)

        return list_of_random_grades

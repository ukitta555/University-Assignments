from typing import List

from instructor import Instructor


class Course:
    def __init__(self, number: str, name: str, instructors: List[Instructor], max_number_of_students: int):
        self.number = number
        self.name = name
        self.max_number_of_students = max_number_of_students
        self.instructors = instructors

    def __str__(self):
        return self.name
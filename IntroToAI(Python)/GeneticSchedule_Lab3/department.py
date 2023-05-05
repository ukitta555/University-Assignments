from typing import List

from course import Course


class Department:
    def __init__(self, name: str, courses: List[Course]):
        self.name = name
        self.courses = courses

    def __str__(self):
        return f"Department {self.name}"
from typing import Optional

from course import Course
from department import Department
from instructor import Instructor
from meeting_time import MeetingTime
from room import Room


class UniClass:
    def __init__(self, id: int, department: Department, course: Course):
        self.id = id
        self.department = department
        self.course = course
        self.instructor: Optional[Instructor] = None
        self.meeting_time: Optional[MeetingTime] = None
        self.room: Optional[Room] = None

    def __str__(self):
        return f"{self.department}, {self.course}, {self.room}, {self.instructor}, {self.meeting_time}"
import random
from typing import List

from data import Data
from uni_class import UniClass


class Schedule:
    def __init__(self, data):
        self.data: Data = data
        self.classes: List[UniClass] = []
        self.number_of_conflicts = 0
        self.fitness = -1
        self.schedule_class_id = 0

    def initialize(self):
        departments = self.data.departments
        for department in departments:
            for course in department.courses:
                uni_class = UniClass(self.schedule_class_id, department, course)
                self.schedule_class_id += 1
                uni_class.meeting_time = random.choice(self.data.meeting_times)
                uni_class.room = random.choice(self.data.rooms)
                uni_class.instructor = random.choice(self.data.instructors)
                self.classes.append(uni_class)
        return self

    def calculate_fitness(self):
        self.number_of_conflicts = 0
        for uni_class_index, uni_class in enumerate(self.classes):
            if uni_class.room.seating_capacity < uni_class.course.max_number_of_students:
                self.number_of_conflicts += 1
            if not (uni_class.instructor in uni_class.course.instructors):
                self.number_of_conflicts += 1
            for another_uni_class in self.classes[uni_class_index + 1:]:
                if uni_class.meeting_time == another_uni_class.meeting_time:
                    if uni_class.room == another_uni_class.room:
                        self.number_of_conflicts += 1
                    if uni_class.instructor == another_uni_class.instructor:
                        self.number_of_conflicts += 1


        # + 1 to avoid zero division;
        # in case of many conflicts, the value will approach zero
        return 1 / (self.number_of_conflicts + 1)

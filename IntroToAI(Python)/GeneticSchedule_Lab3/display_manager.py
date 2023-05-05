from prettytable import PrettyTable

from population import Population
from schedule import Schedule


class DisplayManager:
    @staticmethod
    def print_generation(population: Population):
        table = PrettyTable([
            "Schedule #",
            "Fitness",
            "# of conflicts",
            # "Classes"
        ])
        for index, schedule in enumerate(population.schedules):
            table.add_row([
                index,
                round(schedule.calculate_fitness(), 3),
                schedule.number_of_conflicts,
            ])
        print(table)


    @staticmethod
    def print_schedule_as_table(schedule: Schedule):
        table = PrettyTable([
            "Class #",
            "Department",
            "Course",
            "Max # of students for course",
            "Room capacity",
            "Instructor",
            "Class time"
        ])
        for index, uni_class in enumerate(sorted(schedule.classes, key=lambda x: x.meeting_time.id)):
            table.add_row([
                    index,
                    uni_class.department,
                    uni_class.course,
                    uni_class.course.max_number_of_students,
                    uni_class.room.seating_capacity,
                    uni_class.instructor,
                    uni_class.meeting_time
            ])
        print(table)


from course import Course
from department import Department
from instructor import Instructor
from meeting_time import MeetingTime
from room import Room


class Data:
    ROOMS = [["Room 39", 45], ["Room 1", 35], ["Room 41", 25]]
    MEETING_TIMES = [
        [1, "Monday 08:40 - 10:20"],
        [2, "Monday 10:35 - 12:10"],
        [3, "Monday 12:20 - 13:55"],
        [4, "Tuesday 08:40 - 10:20"],
        [5, "Tuesday 10:35 - 12:10"],
        [6, "Tuesday 12:20 - 13:55"],
        [7, "Wednesday 08:40 - 10:20"],
        [8, "Wednesday 10:35 - 12:10"],
        [9, "Wednesday 12:20 - 13:55"],
        [10, "Thursday 08:40 - 10:20"],
        [11, "Thursday 10:35 - 12:10"],
        [12, "Thursday 12:20 - 13:55"],
        [13, "Friday 08:40 - 10:20"],
        [14, "Friday 10:35 - 12:10"],
        [15, "Friday 12:20 - 13:55"],
    ]
    INSTRUCTORS = [
        ["Instructor1", "Andrew Stavrovskyi"],
        ["Instructor2", "Alex Fedorus"],
        ["Instructor3", "Yuliia Shevchuk"],
        ["Instructor4", "Oleksandr Derevyanchenko"],
        ["Instructor5", "Igor Zavadskyii"],
        ["Instructor6", "Andrii Anikushin"],
        ["Instructor7", "Vyacheslav Rabanovich"],
        ["Instructor8", "Tetiana Karnaukh"],
        ["Instructor9", "Roman Yakimiv"],
    ]

    def __init__(self):
        self.rooms = []
        self.meeting_times = []
        self.instructors = []
        self.courses = []
        for room in self.ROOMS:
            self.rooms.append(Room(number=room[0], seating_capacity=room[1]))
        for meeting_time in self.MEETING_TIMES:
            self.meeting_times.append(MeetingTime(id=meeting_time[0], time=meeting_time[1]))
        for instructor in self.INSTRUCTORS:
            self.instructors.append(Instructor(id=instructor[0], name=instructor[1]))

        discrete_math_lectures = Course(
            number="L1",
            name="Discrete Math (lecture)",
            instructors=[self.instructors[0]],
            max_number_of_students=25
        )
        discrete_math_practice = Course(
            number="P1",
            name="Discrete Math (practice)",
            instructors=[self.instructors[0], self.instructors[1], self.instructors[2]],
            max_number_of_students=35,
        )
        programming_lectures = Course(
            number="L2",
            name="Programming (lecture)",
            instructors=[self.instructors[0], self.instructors[2]],
            max_number_of_students=25
        )
        programming_practice = Course(
            number="P2",
            name="Programming (practice)",
            instructors=[self.instructors[0], self.instructors[2], self.instructors[3]],
            max_number_of_students=30
        )
        cloud_technologies_lecture = Course(
            number="L3",
            name="Cloud (lectures)",
            instructors=[self.instructors[3]],
            max_number_of_students=35
        )
        computer_networking_lecture = Course(
            number="L4",
            name="Computer Networking (lectures)",
            instructors=[self.instructors[2]],
            max_number_of_students=45
        )
        computer_networking_practice = Course(
            number="P4",
            name="Computer Networking (practice)",
            instructors=[self.instructors[1], self.instructors[2]],
            max_number_of_students=30
        )
        quantum_computations = Course(
            number="L5",
            name="Quantum Computations (lectures)",
            instructors=[self.instructors[4]],
            max_number_of_students=45
        )
        calculus = Course(
            number="L6",
            name="Calculus (lectures)",
            instructors=[self.instructors[5],self.instructors[6]],
            max_number_of_students=45
        )
        calculus_practice = Course(
            number="P6",
            name="Calculus (practice)",
            instructors=[self.instructors[5], self.instructors[6]],
            max_number_of_students=25
        )
        linear_algebra = Course(
            number="L7",
            name="Linear Algebra (lectures)",
            instructors=[self.instructors[6]],
            max_number_of_students=36
        )
        linear_algebra_practice = Course(
            number="P7",
            name="Linear Algebra (practice)",
            instructors=[self.instructors[6]],
            max_number_of_students=26
        )
        automata_theory = Course(
            number="L8",
            name="Automata Theory (lectures)",
            instructors=[self.instructors[7], self.instructors[0]],
            max_number_of_students=45
        )
        automata_theory_practice = Course(
            number="P8",
            name="Automata Theory (practice)",
            instructors=[self.instructors[7], self.instructors[0]],
            max_number_of_students=15
        )
        operations_research = Course(
            number="L9",
            name="Operations Research (lectures)",
            instructors=[self.instructors[8]],
            max_number_of_students=25
        )
        operation_research_practice = Course(
            number="P9",
            name="Operations Research (practice)",
            instructors=[self.instructors[8]],
            max_number_of_students=15
        )
        applied_algorithms = Course(
            number="L10",
            name="Applied Algorithms (lectures)",
            instructors=[self.instructors[4]],
            max_number_of_students=25
        )

        self.courses = [
            discrete_math_lectures,
            discrete_math_practice,
            programming_practice,
            programming_lectures,
            cloud_technologies_lecture,
            computer_networking_practice,
            computer_networking_lecture,
            quantum_computations,
            calculus,
            calculus_practice,
            linear_algebra,
            linear_algebra_practice,
            operations_research,
            operation_research_practice,
            automata_theory,
            automata_theory_practice,
            applied_algorithms,
        ]
        theoretical_cs_department = Department(
            name="TK",
            courses=[programming_lectures, programming_practice, discrete_math_lectures, discrete_math_practice,
                     automata_theory, automata_theory_practice]
        )
        mathematical_informatics_department = Department(
            name="MI",
            courses=[cloud_technologies_lecture, quantum_computations, applied_algorithms]
        )
        system_analysis_department = Department(
            name="SA",
            courses=[computer_networking_practice, computer_networking_lecture]
        )
        operation_research_department = Department(
            name="DO",
            courses=[linear_algebra, linear_algebra_practice, operations_research, operation_research_practice]
        )
        computational_mathematics_department = Department(
            name="OM",
            courses=[calculus, calculus_practice]
        )
        self.departments = [
            theoretical_cs_department,
            mathematical_informatics_department,
            system_analysis_department,
            operation_research_department,
            computational_mathematics_department
        ]
        self.number_of_classes = 0
        for department in self.departments:
            self.number_of_classes += len(department.courses)
from typing import List


from data import Data
from schedule import Schedule


class Population:
    def __init__(self, data: Data, size: int):
        self.size = size
        self.data = data
        self.schedules: List[Schedule] = []
        for i in range(size):
            schedule = Schedule(data=data)
            schedule.initialize()
            self.schedules.append(schedule)
        self.schedules.sort(key=lambda x: x.calculate_fitness(), reverse=True)



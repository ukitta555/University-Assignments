import random

from consts import ELITE_SCHEDULES_GROUP_SIZE, POPULATION_SIZE, CROSSOVER_THRESHOLD, MUTATION_THRESHOLD, \
    TOURNAMENT_POPULATION_SIZE
from data import Data
from population import Population
from schedule import Schedule


class GeneticAlgorithm:
    def evolve(self, population: Population, data: Data):
        return self.mutate_population(
            population=self.crossover_population(population=population, data=data),
            data=data
        )

    def crossover_population(self, data: Data, population: Population):
        # create empty population as a starting point
        crossover_population = Population(data=data, size=0)
        for elite_schedule_index in range(ELITE_SCHEDULES_GROUP_SIZE):
            crossover_population.schedules.append(population.schedules[elite_schedule_index])
        for normal_schedule_index in range(ELITE_SCHEDULES_GROUP_SIZE, POPULATION_SIZE):
            first_parent = self.tournament_schedule_selection(population=population, data=data)
            second_parent = self.tournament_schedule_selection(population=population, data=data)
            crossover_population.schedules.append(
                self.crossover_schedules(
                    first_parent=first_parent,
                    second_parent=second_parent,
                    data=data
                )
            )
        return crossover_population

    def crossover_schedules(self, first_parent: Schedule, second_parent: Schedule, data: Data):
        crossover_schedule = Schedule(data=data).initialize()
        for class_number in range(len(crossover_schedule.classes)):
            if random.uniform(0, 1) > CROSSOVER_THRESHOLD:
                crossover_schedule.classes[class_number] = first_parent.classes[class_number]
            else:
                crossover_schedule.classes[class_number] = second_parent.classes[class_number]
        return crossover_schedule

    def mutate_population(self, population: Population, data: Data):
        for normal_schedule_index in range(ELITE_SCHEDULES_GROUP_SIZE, POPULATION_SIZE):
            self.mutate_schedule(population.schedules[normal_schedule_index], data=data)
        return population

    def mutate_schedule(self, schedule: Schedule, data: Data):
        random_schedule = Schedule(data=data).initialize()
        for class_index in range(len(schedule.classes)):
            if random.uniform(0, 1) < MUTATION_THRESHOLD:
                schedule.classes[class_index] = random_schedule.classes[class_index]
        return schedule

    def tournament_schedule_selection(self, data: Data, population: Population):
        tournament_population = Population(data=data, size=0)
        for random_selection_trial in range(TOURNAMENT_POPULATION_SIZE):
            tournament_population.schedules.append(random.choice(population.schedules))
        tournament_population.schedules.sort(key=lambda x: x.calculate_fitness(), reverse=True)
        return tournament_population.schedules[0]

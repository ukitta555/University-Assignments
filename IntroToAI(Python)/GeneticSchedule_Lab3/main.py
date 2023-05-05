from consts import POPULATION_SIZE
from data import Data
from display_manager import DisplayManager
from genetic_algorithm import GeneticAlgorithm
from population import Population

if __name__ == '__main__':
    data = Data()
    population = Population(data=data, size=POPULATION_SIZE)
    display_manager = DisplayManager()
    display_manager.print_generation(population=population)
    display_manager.print_schedule_as_table(schedule=population.schedules[0])
    genetic_algorithm = GeneticAlgorithm()
    while population.schedules[0].calculate_fitness() != 1.0:
        population = genetic_algorithm.evolve(
            population=population,
            data=data
        )
        population.schedules.sort(key=lambda x: x.calculate_fitness(), reverse=True)
        display_manager.print_generation(population=population)
        display_manager.print_schedule_as_table(schedule=population.schedules[0])
    print("\n\n")

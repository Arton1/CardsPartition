from evolutional_algorithm.population import Population
from config import Config
from sys import argv
import cProfile

amount_of_cards = 10
A = 30
B = 100
config = Config("./consts.config")
population = Population(amount_of_cards, A, B)
population.print_information()
population.print_statistics()
for step in range(config.get_max_generation()):
    population.evolve()
    population.print_generation()
    population.print_information()
    population.print_statistics()

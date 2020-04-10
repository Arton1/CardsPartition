from evolutional_algorithm.population import Population
from config import Config
from sys import argv
import cProfile


if len(argv) != 4:
    print("Usage: python main.py amount_of_cards A B")
    exit()
amount_of_cards = int(argv[1])
A = int(argv[2])
B = int(argv[3])
config = Config("consts.config")
population = Population(amount_of_cards, A, B)
population.print_information()
population.print_statistics()
for step in range(config.get_max_generation()):
    population.evolve()
    population.print_generation()
    population.print_information()
    population.print_statistics()

from evolutional_algorithm.population import Population
from config import Config
from sys import argv
import cProfile


if len(argv) != 5:
    print("Usage: python main.py amount_of_cards A B threshold_in_percentage")
    exit()
amount_of_cards = int(argv[1])
a = int(argv[2])
b = int(argv[3])
threshold = float(argv[4].strip("%"))/100
config = Config("consts.config")
population = Population(amount_of_cards, a, b, threshold)
population.print_information()
population.print_statistics()
population.evolve()
    

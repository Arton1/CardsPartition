from evolutional_algorithm.population import Population
import config
from sys import argv
import cProfile

amount_of_cards = 10
A = 30
B = 100
population = Population(amount_of_cards, A, B)
# population.print_information()
population.print_statistics()
for step in range(15):
    population.evolve()
    population.print_generation()
    # population.print_information()
    population.print_statistics()

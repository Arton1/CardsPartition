from evolutional_algorithm.population import Population
from sys import argv
import cProfile

amount_of_cards = 10
A = 30
B = 100
population = Population(amount_of_cards, A, B)
population.print_information()
for step in range(5):
    population.evolve()
    population.print_information()

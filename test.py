from evolutional_algorithm.population import Population
from config import Config
from sys import argv


def print_average_fitness(population):
    print(f"Średnia wartość funkcji celu: {population.get_generations_average_fitness()}")


def print_best_fitness(population):
    print(f"Najlepsza wartość funkcji celu: {population.get_generations_best_fitness()}")


def print_threshold_fitness(population):
    print(f"Dopasowanie najlepszego osobnika: A: {population.get_generations_A_threshold_fitness()} B: {population.get_generations_B_threshold_fitness()}")


def print_informations(population):
    population.print_candidates_info()
    print_average_fitness(population)
    print_best_fitness(population)
    print_threshold_fitness(population)
    while population.evolveOnce():
        population.print_candidates_info()
        print_average_fitness(population)
        print_best_fitness(population)
        print_threshold_fitness(population)


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: python main.py amount_of_cards A B threshold_in_percentage")
        exit()
    amount_of_cards = int(argv[1])
    a = int(argv[2])
    b = int(argv[3])
    threshold = float(argv[4].strip("%"))/100
    config = Config("consts.config")
    population = Population(amount_of_cards, a, b, threshold)
    print_informations(population)
        

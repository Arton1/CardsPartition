from evolutional_algorithm.population import Population
from config import Config
from sys import argv


def printMultipleExecutionsInformations(amount_of_executions):
    average_fitness_sum_list = [0]*(Population._MAX_GENERATION+1)
    best_fitness_sum_list = [0]*(Population._MAX_GENERATION+1)
    amount_of_executions_for_generation = [0]*(Population._MAX_GENERATION+1)
    for execution in range(amount_of_executions):
        population = Population(amount_of_cards, a, b, threshold)
        average_fitness_sum_list[population.get_generation()] += population.get_generations_average_fitness()
        best_fitness_sum_list[population.get_generation()] += population.get_generations_best_fitness()
        amount_of_executions_for_generation[population.get_generation()] += 1
        while(population.evolveOnce()):
            average_fitness_sum_list[population.get_generation()] += population.get_generations_average_fitness()
            best_fitness_sum_list[population.get_generation()] += population.get_generations_best_fitness()
            amount_of_executions_for_generation[population.get_generation()] += 1
    print(f"Średnie wartości {amount_of_executions} uruchomień:")
    print(f"Generacja : średnia wartość f. przystosowania : najlepsza wartość f. przystosowania : liczba wywołań generacji")
    for (index, average_fitness_sum), best_fitness_sum, amount_of_generations_executions in zip(enumerate(average_fitness_sum_list), best_fitness_sum_list, amount_of_executions_for_generation):
        if(amount_of_generations_executions > 0):
            print(f"{index} : {average_fitness_sum/amount_of_generations_executions} : {best_fitness_sum/amount_of_generations_executions} : {amount_of_generations_executions}")
        else:
            print(f"{index} : Brak wywołań")


if __name__ == "__main__":
    if len(argv) != 6:
        print("Usage: python main.py amount_of_cards A B threshold_in_percentage amount_of_executions")
        exit()
    amount_of_cards = int(argv[1])
    a = int(argv[2])
    b = int(argv[3])
    threshold = float(argv[4].strip("%"))/100
    config = Config("consts.config")
    printMultipleExecutionsInformations(int(argv[5]))
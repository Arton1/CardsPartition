from evolutional_algorithm.population import Population
from config import Config
from sys import argv
from math import fabs

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
    population.evolve()
    A_list, B_list = population.get_best_solution()
    print(f"Pierwszy stos: {A_list}")
    print(f"Drugi stos: {B_list}")
    sum_A = sum(A_list)
    print(f"Suma pierwszego stosu = {sum(A_list)} (Dopasowanie: {1-(fabs(a-sum_A)/a):.3f})")
    product_B = 1
    for card in B_list:
        product_B *= card
    print(f"Iloczyn drugiego stosu = {product_B} (Dopasowanie: {1-(fabs(b-product_B)/b):.3f})")
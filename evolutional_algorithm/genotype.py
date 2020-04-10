from random import randint, random, sample, uniform
from math import ceil, floor, pi


class Genotype:
    _AMOUNT_OF_CROSSOVER_POINTS = 6
        
    def __init__(self):
        self._fitness = float("inf")

    def evaluate_fitness(self, position):
        pass
    
    def get_fitness(self):
        return self._fitness

    def create_pair_by_multipoints(self, other_parent):
        indexes = sorted(sample(range(0, len(first_parent_genes)-1), self._AMOUNT_OF_CROSSOVER_POINTS))
        first_child_genes = []
        second_child_genes = []
        indexes_index = 0
        switched = False
        for (index, first_parent_gene), second_parent_gene in zip(enumerate(first_parent_genes), second_parent_genes):
            if(switched):
                first_child_genes.append(second_parent_gene)
                second_child_genes.append(first_parent_gene)
            else:
                first_child_genes.append(first_parent_gene)
                second_child_genes.append(second_parent_gene)
            if(indexes_index < len(indexes) and index == indexes[indexes_index]):
                indexes_index += 1
                switched = not switched
        return first_child, second_child

    def mutate(self):
        pass
from random import random, sample
from math import sqrt


class Genotype:
    def __init__(self, created_genes):
        self._fitness = None
        self._genes = created_genes

    def set_constants(amount_of_crossover_points, mutation_probability):
        # called by Config class
        Genotype._AMOUNT_OF_CROSSOVER_POINTS = amount_of_crossover_points
        Genotype._MUTATION_PROBABILITY = mutation_probability

    def get_cards_sum_and_product(self):
        first_stack_sum = 0
        second_stack_product = 1
        for card_value, gene in enumerate(self._genes, start=1):
            if gene == 0:
                first_stack_sum += card_value
            elif gene == 1:
                second_stack_product *= card_value
            else:
                raise ValueError("Inapproriate gene value")
        return first_stack_sum, second_stack_product

    def evaluate_fitness(self, atarget, btarget):
        first_stack_sum, second_stack_product = self.get_cards_sum_and_product()
        self._fitness = sqrt((first_stack_sum-atarget)**2 + (second_stack_product-btarget)**2)

    def get_fitness(self):
        return self._fitness

    def create_pair_by_multipoints(self, other_parent):
        indexes = sorted(sample(range(0, len(self._genes)-1), self._AMOUNT_OF_CROSSOVER_POINTS))
        first_child_genes = []
        second_child_genes = []
        indexes_index = 0
        switched = False
        for (index, first_parent_gene), second_parent_gene in zip(enumerate(self._genes), other_parent._genes):
            if(switched):
                first_child_genes.append(second_parent_gene)
                second_child_genes.append(first_parent_gene)
            else:
                first_child_genes.append(first_parent_gene)
                second_child_genes.append(second_parent_gene)
            if(indexes_index < len(indexes) and index == indexes[indexes_index]):
                indexes_index += 1
                switched = not switched
        return Genotype(first_child_genes), Genotype(second_child_genes)

    def mutate(self):
        for gene in self._genes:
            if random() <= self._MUTATION_PROBABILITY:
                if gene == 0:
                    gene = 1
                else:
                    gene = 0

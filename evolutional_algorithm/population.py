from .genotype import Genotype
from random import randint, random, uniform, sample, seed
from math import ceil, pi


class Population:
    def __init__(self,
                 amount_of_cards,
                 atarget,
                 btarget,
                 ):
        self._atarget = atarget
        self._btarget = btarget
        self._candidates = []
        self._generation = 0
        self._create_starting_population(amount_of_cards)

    def set_constants(amount_of_candidates, amount_of_children, tournament_size):
        # called by Config class
        Population._AMOUNT_OF_CANDIDATES = amount_of_candidates
        Population._AMOUNT_OF_CHILDREN = amount_of_children
        Population._TOURNAMENT_SIZE = tournament_size

    def _create_starting_population(self, amount_of_cards, seed_value=None):
        if seed_value is not None:
            seed(seed_value)
        for candidate in range(self._AMOUNT_OF_CANDIDATES):
            genes = [randint(0, 1) for card in range(amount_of_cards)]
            genotype = Genotype(genes)
            genotype.evaluate_fitness(self._atarget, self._btarget)
            self._candidates.append(genotype)
        print(len(self._candidates))
        if seed_value is not None:
            seed()

    def print_generation(self):
        print(f"Generacja: {self._generation}")

    def print_information(self):
        print(f"A = {self._atarget} B = {self._btarget}")
        for index, genotype in enumerate(sorted(self._candidates, key=lambda x: x.get_fitness())):
            first_stack_sum, second_stack_product = genotype.get_cards_sum_and_product()
            fitness = genotype.get_fitness()
            print(f"{index + 1} : {first_stack_sum} : {second_stack_product} : {fitness}")

    def print_statistics(self):
        sum = 0
        for genotype in self._candidates:
            sum += genotype.get_fitness()
        print(f"Średnia: {sum/len(self._candidates)}")

    def _set_best(self):
        best_fitness = self._best_genotype.get_fitness()
        for genotype in self._candidates:
            genotype_fitness = genotype.get_fitness()
            if best_fitness > genotype.get_fitness():
                best = genotype
                best_fitness = genotype_fitness
        self._best_genotype = best

    def _roulette_select_individual(self, candidates):
        fitness_sum = sum(candidate.get_fitness() for candidate in candidates)
        spin = random()
        probability_sum = 0
        for potential_parent in candidates:
            fitness = potential_parent.get_fitness()
            probability = fitness / fitness_sum
            probability_sum += probability
            if probability_sum > spin:
                return potential_parent

    def _tournament_select_individual(self, candidates):
        tournament_candidates = []
        # for fighter in range(self._tournament_size):
            # tournament_candidates.append(candidates[randint(0, len(candidates)-1)]) # ze zwracaniem
        tournament_candidates = sample(candidates, self._TOURNAMENT_SIZE) # bez zwracania
        return min(tournament_candidates, key=lambda x: x.get_fitness())

    def _ranking_select_individual(self, candidates):
        candidates.sort(key=lambda x: x.get_fitness())
        rank_sum = (len(candidates) + 1) * len(candidates) / 2
        spin = randint(0, rank_sum)
        index_sum = 0
        for index, candidate in enumerate(candidates, start=1):
            if spin <= index_sum + index:
                return candidate
            index_sum += index

    def _best_select_individual(self, candidates_with_fitness):
        return max(candidates_with_fitness, key=lambda x: x.get_fitness())

    def _select_pair_of_parents(self):
        first_parent = self._tournament_select_individual(self._candidates)
        self._candidates.remove(first_parent)
        second_parent = self._tournament_select_individual(self._candidates)
        self._candidates.append(first_parent)
        return first_parent, second_parent

    def _create_children(self):
        children = []
        for pair_of_parents in range(0, self._AMOUNT_OF_CHILDREN, 2):
            first_parent, second_parent = self._select_pair_of_parents()
            pair_of_children = Genotype.create_pair_by_multipoints(first_parent, second_parent)
            for child in pair_of_children:
                child.mutate()
                child.evaluate_fitness(self._atarget, self._btarget)
                children.append(child)
        return children

    def _update_population(self, children):
        self._candidates = sorted(children + self._candidates, key=lambda x: x.get_fitness())[0:len(self._candidates)]

    def evolve(self, amount_of_iterations=1):
        for i in range(amount_of_iterations):
            children = self._create_children()
            self._update_population(children)
            self._generation += 1

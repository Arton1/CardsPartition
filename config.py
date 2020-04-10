from evolutional_algorithm import genotype, population


class Config:
    def __init__(self, file_name):
        self._dict_values = dict()
        with open(file_name, "r") as file:
            for line in file:
                key, value = line.strip("\n").split("=")
                self._dict_values[key] = value
        population.Population.set_constants(self.get_population_size(), self.get_amount_of_children(), self.get_tournament_size())
        genotype.Genotype.set_constants(self.get_amount_of_crossover_points(), self.get_mutation_probability())

    def get_max_generation(self):
        return int(self._dict_values["max generation"])

    def get_population_size(self):
        return int(self._dict_values["population size"])

    def get_amount_of_children(self):
        return int(self._dict_values["amount of children"])

    def get_tournament_size(self):
        return int(self._dict_values["tournament size"])

    def get_mutation_probability(self):
        return float(self._dict_values["mutation probability"])

    def get_amount_of_crossover_points(self):
        return int(self._dict_values["crossover points amount"])
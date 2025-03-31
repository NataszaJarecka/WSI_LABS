import random
import numpy as np

class Individual:

    def __init__(self, genotype, mutation_prob):

        self.genotype = genotype
        self.mutation_prob = mutation_prob

    def get_genotype(self):
        return self.genotype


    def reproduce(self, other_individual):
        gene_count = len(self.genotype)
        cross_point = random.randint(1, gene_count - 1)

        child1 = np.concatenate((self.genotype[:cross_point], other_individual.genotype[cross_point:]))
        child2 = np.concatenate((other_individual.genotype[:cross_point], self.genotype[cross_point:]))

        return Individual(child1, self.mutation_prob), Individual(child2, self.mutation_prob)


    def mutate(self):

        i = 0
        for gene in self.genotype:
            rnd_int = random.randint(1,100)

            if rnd_int/100 < self.mutation_prob:
                self.genotype[i] = abs(gene - 1)
            i += 1

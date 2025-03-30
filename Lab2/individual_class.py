import random

class Individual:

    def __init__(self, genotype, mutation_prob):

        self.genotype = genotype
        self.mutation_prob = mutation_prob

    def get_genotype(self):
        return self.genotype


    def reproduce(self, other_individual):

        gene_count = len(self.genotype)
        cross_point =  random.randint(1, gene_count - 1)
        child1 = self.genotype[:cross_point]+other_individual.genotype[cross_point:]
        child2 = other_individual.genotype[:cross_point]+ self.genotype[cross_point:]

        return Individual(child1, self.mutation_prob), Individual(child2, self.mutation_prob)


    def mutate(self):
        rnd_int = random.randint(1,100)

        if rnd_int/100 < self.mutation_prob:
            gene_count = len(self.genotype)
            rnd_index = random.randint(0,gene_count - 1)
            self.genotype[rnd_index] = abs(self.genotype[rnd_index] - 1)



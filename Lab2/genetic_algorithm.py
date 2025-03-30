import random
from evaluation import evaluate
from individual_class import Individual

def generate_population(gene_count, population_count, mutation_prob):
    population = []

    for individual in range(population_count):
        genotype = []
        for gene in range(gene_count):
            gene = random.randint(0,1)
            genotype.append(gene)
        individual = Individual(genotype, mutation_prob)
        population.append(individual)

    return population

def roulette_selection(population, evaluation, size):

    population_rate = []

    for individual in population:
        rate = evaluation(individual.get_genotype(), size)
        population_rate.append(rate)

    rate_sum = sum(population_rate)
    rnd_int = random.uniform(0, rate_sum)

    cumulated_sum = 0
    for i, rate in enumerate(population_rate):
        cumulated_sum += rate
        if cumulated_sum >= rnd_int:
            return population[i]


def find_the_best(population, evaluation, size):
    population_rate = []

    for individual in population:
        rate = evaluation(individual.get_genotype(), size)
        population_rate.append(rate)
    individual_index = population_rate.index(max(population_rate))
    return population[individual_index]



def genetic_algorithm(evaluation, gene_count, size, population_count, mutation_prob, generations):

    i = 1
    population = generate_population(gene_count, population_count, mutation_prob)
    while i <= generations:


        new_population = []
        for k in range(population_count//2):
            parent1 = roulette_selection(population, evaluation, size)
            parent2 = roulette_selection(population, evaluation, size)
            child1, child2 = parent1.reproduce(parent2)

            child1.mutate()
            child2.mutate()


            new_population.append(child1)
            new_population.append(child2)

        population = new_population
        i += 1

    return find_the_best(population, evaluation, size)



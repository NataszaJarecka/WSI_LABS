import random
from evaluation import evaluate

def generate_population(gene_count, population_count):
    population = []

    for individual in range(population_count):
        individual = []

        for gene in range(gene_count):
            gene = random.randint(0,1)
            individual.append(gene)
        population.append(individual)

    return population


def genetic_algorithm(evaluation, gene_count, size, population_count):
    population = generate_population(gene_count, population_count)




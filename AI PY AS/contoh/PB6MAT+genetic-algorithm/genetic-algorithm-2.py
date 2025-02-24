import random
import numpy as np
import matplotlib.pyplot as plt

# Define the function to optimize (maximize)
def func(x):
    return -x**2 + 3*x + 4

# Genetic Algorithm Parameters
POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7

# Initialize population with random solutions
def init_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

# Evaluate fitness of each solution
def evaluate_fitness(population):
    return [func(x) for x in population]

# Select parents using tournament selection
def select_parents(population, fitness):
    parents = []
    for _ in range(POPULATION_SIZE):
        tournament = random.sample(range(POPULATION_SIZE), 3)
        winner = tournament[np.argmax([fitness[i] for i in tournament])]
        parents.append(population[winner])
    return parents

# Perform crossover
def crossover(parents):
    offspring = []
    for _ in range(POPULATION_SIZE):
        parent1, parent2 = random.sample(parents, 2)
        if random.random() < CROSSOVER_RATE:
            child = (parent1 + parent2) / 2
        else:
            child = parent1
        offspring.append(child)
    return offspring

# Perform mutation
def mutate(offspring):
    for i in range(POPULATION_SIZE):
        if random.random() < MUTATION_RATE:
            offspring[i] += random.uniform(-1, 1)
    return offspring

# Main genetic algorithm loop
def genetic_algorithm():
    population = init_population(POPULATION_SIZE)
    for generation in range(GENERATIONS):
        fitness = evaluate_fitness(population)
        parents = select_parents(population, fitness)
        offspring = crossover(parents)
        offspring = mutate(offspring)
        population = offspring
        print(f"Generation {generation+1}, Best Fitness: {max(fitness)}")
    return population

# Run the genetic algorithm
final_population = genetic_algorithm()

# Plot the function and the final population
x_values = np.linspace(-10, 10, 400)
y_values = func(x_values)
plt.plot(x_values, y_values)
plt.scatter(final_population, [func(x) for x in final_population], c='r')
plt.show()

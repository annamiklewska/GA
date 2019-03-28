import generate_points as pts
import numpy as np
import random
import itertools

M = 2  # degree of the polynomial separating points
points = pts.Points(M)
domain = pts.Points.domain
pop_size = 50
generations = 10
mutation_operator = 2 # no of parents mating


def generate_individual(m):
    '''
    :param m: no of parameters (equal to degree of polynomial)
    :return: vector of arguments (starting with x^0); mx1
    individual is a vector of parameters of a polynomial function
    '''
    return np.random.randint(-10, 10, m)


def generate_population(p_size, m):
    '''
    :param p_size: no of individuals in a population
    :param m: degree of polynomial = no of genes in an individual
    :return: matrix of vectors of parameters - a population
    '''
    return [generate_individual(m) for i in range(p_size)]


def crossover(p1, p2):
    """
    :param p1: vector of parameters
    :param p2: vector of parameters
    :return: vector of parameters (child = first half of p1 + second part of p2)
    If the length of child is uneven, more values are taken from parent2
    """
    k = len(p1)
    j = int(k/2)
    a = [p1[i] for i in range(0, j)]
    b = [p2[i] for i in range(j, k)]
    child = a + b
    return child


def mutation(individual, no_mutations):
    print("before loop: ", individual)
    for i in range(no_mutations):
        x = random.randint(0, (len(individual) - 1))
        a = random.randint(-10, 10)
        individual[x] = a
        print("rand: ", a)
        print(individual[x])
    return individual


def fitness_fun():
    pass


N = 3
w = generate_individual(N)
z = generate_individual(N)
j = crossover(w, z)
h = mutation(w, mutation_operator)
print("individual before, after: ", w, h)


# define mutation operator

# define selection operator

# initialise population


# visualisation

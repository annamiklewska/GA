import generate_points as pts
import numpy as np
import random
import itertools
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as p

M = 2  # degree of the polynomial separating points = length of individual
points = pts.Points(M)
domain = pts.Points.domain
pop_size = 50
generations = 10
mutation_operator = 2  # no of parents mating


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
    '''
    :param individual: vector of parameters
    :param no_mutations: no of changes that should be made
    :return: vector of parameters after mutation [by value so individual is changed already]
    '''
    for i in range(no_mutations):
        x = random.randint(0, (len(individual) - 1))
        a = random.randint(-10, 10)
        individual[x] = a
    return individual  # due to the way python works individual is already changed


def fitness_fun(individual, points_above, points_below):
    err = 0
    line = p.polyval(domain, individual)  # vector of points
    for i in range(domain):
        if line[i] >= points_above[i]:
            err += 1
        if line[i] <= points_below[i]:
            err += 1
    return err




w = generate_individual(M)
z = generate_individual(M)
j = crossover(w, z)
h = mutation(w, mutation_operator)
print("individual after mutation: ", h)


# visualisation

import generate_points as pts
import numpy as np
import random
import itertools

points = pts.Points(2)
domain = pts.Points.domain
pop_size = 50
generations = 10


def generate_individual(N):
    '''
    :param N: no of parameters (equal to degree of polynomial)
    :return: vector of arguments (starting with x^0); Nx1
    individual is a vector of parameters of a polynomial function
    '''
    return np.random.uniform(-10, 10, N)


def generate_population(pop_size, N):
    '''
    :param pop_size: no of individuals in a population
    :param N: degree of polynomial = no of genes in an individual
    :return: matrix of vectors of parameters - a population
    '''
    return [generate_individual(N) for i in range(pop_size)]

# define fitness function

# define crossover operation
def crossover(p1, p2):
    k = len(p1)  # 5
    j = int(k/2)  # 2
    print(j, k)
    a = p1[0:(j+1)]
    b = p2[(j+1):k]
    print("p1: ", p1)
    print("p2: ", p2)
    print("a: ", a)
    print(len(a))
    print("b: ", b)
    a = a + b
    print(a)
    return a
    pass

N = 5
w = generate_individual(N)
z = generate_individual(N)
j = crossover(w, z)
print(w, z)
k = 3
g = w[0:k]
print(g)
print("nothing to see here", g)
print(j)


# define mutation operator

# define selection operator

# initialise population


# visualisation

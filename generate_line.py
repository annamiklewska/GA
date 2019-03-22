import numpy as np
import random
import matplotlib.pyplot as plt

class Points:
    x_axis = np.linspace(0, 10, 100)

    def polynomial(self, x, w):
        dm = [w[i] * x**i for i in range(np.shape(w)[0])]
        return np.sum(dm, axis=0)


def polynomial(x, w):
    dm = [w[i] * x**i for i in range(len(w))]  # np.shape(w)[0] = no. of rows
    return np.sum(dm, axis=0)


def solution02 ():

    def y(x, m, b):
        return m * x + b

    m = random.random()*10*random.choice((-1, 1))
    b = random.random()*10
    w = np.array([b, m])

    X = np.linspace(0, 10, 100) # 100 evenly distributed points in range 0-10
    #y_above = [y(x, m, b) + (abs(random.gauss(10, 50))+5) for x in X]
    #y_below = [y(x, m, b) - (abs(random.gauss(10, 50))+5) for x in X]
    y_above = [polynomial(X, w) + (abs(random.gauss(10, 50)) + 5)]
    y_below = [polynomial(X, w) - (abs(random.gauss(10, 50)) + 5)]

    import matplotlib.pyplot as plt
    plt.scatter(X, y_below, c='g')
    plt.scatter(X, y_above, c='r')
    #plt.plot(X, y(X, m, b))
    plt.plot(X, polynomial(X, w))
    plt.show()
    print(polynomial(X, w))

    '''
    def solution00():
        m, b = 1, 0
        lower, upper = -25, 25

        num_points = 10

        x1 = [random.randrange(start=1, stop=9) for i in range(num_points)]
        x2 = [random.randrange(start=1, stop=9) for j in range(num_points)]

        y1 = [random.randrange(start=lower, stop=m * x + b) for x in x1]
        y2 = [random.randrange(start=m * x + b, stop=upper) for x in x2]

        plt.plot(np.arange(10), m * np.arange(10) + b)
        plt.scatter(x1, y1, c='blue')
        plt.scatter(x2, y2, c='red')
    '''
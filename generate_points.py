import numpy as np
import random
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as p


class Points:
    #domain = np.linspace(0, 10, 200)  # 100 evenly distributed points in range 0-10
    domain = [random.random()*10 for _ in range(100)]

    def __init__(self, M):
        '''
        :param M: degree of the polynomial separating points
        '''
        self.M = M
        self.w = Points.generate_parameters(self.M)
        self.y_above, self.y_below = Points.generate_points(self.w)

    def get_y_above(self):
        return self.y_above

    def get_y_below(self):
        return self.y_below

    def get_values(self):
        return self.y_above, self.y_below

    @staticmethod
    def polynomial(x, w):  # it was replaced by polyval
        '''
        :param x: vector of arguments (starting with x^0); Nx1
        :param w: vector of parameters; (M-1)x1
        :return: vector of polynomial values for points x; Nx1
        w[0]x[M-1] + w[1]x[M-1] + ... + w[N]x[0]
        w[0]x^M + w[1]x^M-1 + ... + w[N]x^0
        '''
        dm = [w[i] * x ** i for i in range(len(w))]  # np.shape(w)[0] = no. of rows
        return np.sum(dm, axis=0)

    def draw(self):
        domain = Points.domain
        plt.scatter(domain, self.y_below, c='g')
        plt.scatter(domain, self.y_above, c='r')
        plt.plot(domain, p.polyval(domain, self.w))
        plt.axes([-10, -10, 10, 10])
        plt.show()

    @staticmethod
    def generate_points(w):
        '''
        :param w: vector of parameters
        :return: y values of points above and below a polynomial line
        '''
        domain = Points.domain
        mx = abs(max(p.polyval(domain, w)))

        y_above = [p.polyval(domain, w)[i] + (abs(random.gauss(10, 50)) * mx) + 5 for i in range(len(domain))]
        y_below = [p.polyval(domain, w)[i] - (abs(random.gauss(10, 50)) * mx) for i in range(len(domain))]
        return y_above, y_below

    @staticmethod
    def generate_parameters(N):
        '''
        :param N: no of parameters (equal to degree of polynomial)
        :return: vector of parameters (starting with x^0); Nx1
        '''
        # w = np.zeros(N)
        # for i in range(N):
            # w[i] = random.random() * 10 * random.choice((-1, 1))
        # OR
        # w = [random.random() * 10 * random.choice((-1, 1))
        return np.random.randint(-4, 4, N)


'''
def polynomial(x, w):
    dm = [w[i] * x**i for i in range(len(w))]  # np.shape(w)[0] = no. of rows
    return np.sum(dm, axis=0)
'''

'''
def solution02 ():

    def y(x, m, b):
        return m * x + b

    m = random.random()*10*random.choice((-1, 1))
    b = random.random()*10
    w = np.array([b, m])

    domain = np.linspace(0, 10, 100) # 100 evenly distributed points in range 0-10
    #y_above = [y(x, m, b) + (abs(random.gauss(10, 50))+5) for x in domain]
    #y_below = [y(x, m, b) - (abs(random.gauss(10, 50))+5) for x in domain]
    y_above = [polynomial(domain, w)[i] + (abs(random.gauss(10, 50))) + 5 for i in range(len(domain))]
    y_below = [polynomial(domain, w)[i] - (abs(random.gauss(10, 50))) + 5 for i in range(len(domain))]


    plt.scatter(domain, y_below, c='g')
    plt.scatter(domain, y_above, c='r')
    #plt.plot(X, y(X, m, b))
    plt.plot(domain, polynomial(domain, w))
    plt.show()
'''

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

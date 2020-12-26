import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class MF():

    def __init__(self, R, P, Q, userBias, animeBias, K, alpha, beta, iterations):
        """
        Perform matrix factorization to predict empty
        entries in a matrix.

        Arguments
        - R (ndarray)   : user-item rating matrix
        - K (int)       : number of latent dimensions
        - alpha (float) : learning rate
        - beta (float)  : regularization parameter
        """

        self.R = R  # User x Movie  0 represent un-rate shows
        self.P = P # the user matrix with k
        self.Q = Q # anime matrix with k
        # the frame for each user's bias
        self.b_u = userBias
        # the frame for each item's bias
        self.b_i = animeBias
        print(R.shape)
        self.num_users, self.num_items = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations

    def train(self):
        # Initialize user and item latent feature matrix

        """
        self.P = np.random.normal(scale=1. / self.K, size=(self.num_users, self.K)) # the user matrix with k
        self.Q = np.array([
            [0.1, 0.11, 0.21, 0.09, 0.11, 0.112],
            [-0.32, 0, -0.1, 0, -0.12, -0.1],
            [0, -0.12, 0.1, 0, 0, 0],
            [0, 0, 0, 0.1, -0.11, 0]
        ])"""
        #print(self.P)
        #self.Q = np.random.normal(scale=1. / self.K, size=(self.num_items, self.K)) # the movei matrix with k
        # just create the frame, but data inside is random

        # Initialize the biases
        """
        # the frame for each user's bias
        self.b_u = np.zeros(self.num_users)
        # the frame for each item's bias
        self.b_i = np.zeros(self.num_items)"""
        self.b = np.mean(self.R[np.where(self.R != 0)])  # gloab bias, the mean of all rate shows


        # Create a list of training samples
        # this sample only contain user_i, moive_j, and rating that is not equal to 0
        # only contain all rated matrix location
        self.samples = [
            (i, j, self.R[i, j])
            for i in range(self.num_users)
            for j in range(self.num_items)
            if self.R[i, j] > 0
        ]

        #print(self.samples)

        # Perform stochastic gradient descent for number of iterations
        training_process = []
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            mse = self.mse()
            training_process.append((i, mse))
            if (i + 1) % 10 == 0:
                print("Iteration: %d ; error = %.4f" % (i + 1, mse))

        return training_process

    def mse(self):
        """
        A function to compute the total mean square error
        """
        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        for x, y in zip(xs, ys):
            error += pow(self.R[x, y] - predicted[x, y], 2)
        return np.sqrt(error)

    def sgd(self):
        """
        Perform stochastic graident descent
        """
        for i, j, r in self.samples:
            # Computer prediction and error
            prediction = self.get_rating(i, j)
            e = (r - prediction)  # error of real rating minus predict rating

            # Update biases for each show
            self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
            self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])

            # Create copy of row of P since we need to update it but use older values for update on Q
            #print(i, j, r, self.Q[j, :], self.P[i, :])
            P_i = self.P[i, :][:]
            P_i = np.ndarray.copy(self.P[i,:])
            #print(P_i)

            # Update user and item latent feature matrices
            #self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i, :])
            # len(self.P[i,:]) number of k
            #print(i, j, r, self.Q[j, :], self.P[i,:])
            for x in range(self.K):
                if self.Q[j][x] == 0:
                    #print("zero")
                    pass
                else:
                    self.P[i][x] += self.alpha * (e * self.Q[j][x] - self.beta * self.P[i][x])
                    #print(self.P[i, :], self.Q[j, :])
                #print(self.P[i, :], self.Q[j, :])
            for x in range(self.K):
                if self.Q[j][x] == 0:
                    #print("0")
                    pass
                else:
                    self.Q[j][x] += self.alpha * ( e * P_i[x] - self.beta * self.Q[j][x])
            #self.Q[j, :] += self.alpha * (e * P_i - self.beta * self.Q[j, :])

    def get_rating(self, i, j):
        """
        Get the predicted rating of user i and item j
        """
        prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
        return prediction

    def full_matrix(self):
        """
        Computer the full matrix using the resultant biases, P and Q
        """
        return self.b + self.b_u[:, np.newaxis] + self.b_i[np.newaxis:, ] + self.P.dot(self.Q.T)


"""
R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])
"""
"""
mf = MF(R, K=6, alpha=0.01, beta=0.01, iterations=1000)

training_process = mf.train()

print()
print("P x Q:")
print(mf.full_matrix())
print()
print("Global bias:")
print(mf.b)
print()
print("User bias:")
print(mf.b_u)
print()
print("Item bias:")
print(mf.b_i)
"""
import laplacian
import random
import numpy
from matplotlib import pyplot as plt


def blockParition(p, q, n=100):
    print('Checking p={}, q={}'.format(p, q))
    matrix = numpy.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            if i == j:
                continue

            if (i < 50 and j < 50) or (i >= 50 and j >= 50):
                if random.random() < p:
                    matrix[i, j] = 1
            else:
                if random.random() < q:
                    matrix[i, j] = 1

    return matrix


def qualityOfCut(left, right):
    leftLT50 = len([x for x in left if x < 50]) / 50
    leftGT50 = len([x for x in left if x >= 50]) / 50
    rightLT50 = len([x for x in right if x < 50]) / 50
    rightGT50 = len([x for x in right if x >= 50]) / 50

    return max(leftLT50 + rightGT50, leftGT50 + rightLT50)


def plotQualities():
    q = 0.1
    ps = list(reversed(numpy.arange(0.1, 0.5, 0.01)))
    cutQualities = [qualityOfCut(*laplacian.bestCut(blockParition(p, q))) for p in ps]

    plt.plot(ps, cutQualities)
    plt.show()

if __name__ == "__main__":
    plotQualities()

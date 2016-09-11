import random

import matplotlib.pyplot as plt
import numpy

import laplacian


def secondEigenvalue(graph):
    laplacianMatrix = laplacian.laplacian(graph, normalize=True)

    # eigenvalues is a 1-d array of real numbers,
    eigenvalues, _ = numpy.linalg.eig(laplacianMatrix)

    # sort eigenvectors by eigenvalue increasing
    sortedIndices = eigenvalues.argsort()
    eigenvalues = eigenvalues[sortedIndices]

    return eigenvalues[1]


def cycle(n):
    A = numpy.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == ((j + 1) % n):
                A[i, j] = 1
                A[j, i] = 1

    return A


def plotSecondEigenvalue(n=100):
    G = cycle(n)

    # List the edges not in the cycle in random order
    edges = [(i, j) for i in range(n) for j in range(n)
             if i < j and i != ((j + 1) % n)]
    random.shuffle(edges)

    xs = [n + i for i in range(len(edges))]
    print(len(xs))
    ys = []

    for count, edge in enumerate(edges):
        if count % 100 == 0:
            print((count, edge))

        i, j = edge
        G[i, j] = 1
        G[j, i] = 1
        ys.append(secondEigenvalue(G))

    plt.plot(xs, ys)
    plt.show()

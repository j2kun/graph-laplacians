import numpy
import random

exampleMatrix = numpy.array([
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
])


def laplacian(adjacencyMatrix, normalize=False):
    numRows, numCols = adjacencyMatrix.shape
    degrees = numpy.sum(adjacencyMatrix, axis=0)

    if normalize:
        normalizedDegrees = 1 / numpy.sqrt(numpy.array(
            [[degrees[i] * degrees[j] * adjacencyMatrix[i, j] for j in range(numCols)] for i in range(numRows)]
        ))

        # remove inf's created by dividing by zero
        normalizedDegrees[normalizedDegrees == numpy.inf] = 0

        return numpy.diag(numpy.ones(numRows)) - normalizedDegrees
    else:
        combinatorialLaplacian = numpy.diag(degrees) - adjacencyMatrix
        return combinatorialLaplacian


def bestCut(graph):
    laplacianMatrix = laplacian(graph, normalize=True)
    n, m = laplacianMatrix.shape

    # eigenvalues is a 1-d array of real numbers,
    # eigenvectors is a matrix whose **columns** are the corresponding eigenvectors
    eigenvalues, eigenvectors = numpy.linalg.eig(laplacianMatrix)

    # sort eigenvectors by eigenvalue increasing
    sortedIndices = eigenvalues.argsort()
    eigenvalues = eigenvalues[sortedIndices]
    eigenvectors = eigenvectors[:, sortedIndices]

    # sort vertices of G by their value in the second eigenvector
    secondEigenvector = eigenvectors[:, 1]
    sortedVertexIndices = secondEigenvector.argsort()

    def cutQuality(j):
        firstHalf, secondHalf = sortedVertexIndices[range(j+1)], sortedVertexIndices[range(j+1, n)]
        firstTotal, secondTotal, crossTotal = 0, 0, 0

        for u in range(n):
            for v in range(m):
                if graph[u, v] > 0:
                    if u in firstHalf and v in firstHalf:
                        firstTotal += graph[u, v]
                    elif u in secondHalf and v in secondHalf:
                        secondTotal += graph[u, v]
                    else:
                        crossTotal += graph[u, v]

        if 0 == min(firstTotal, secondTotal):
            return numpy.inf

        return crossTotal / min(firstTotal, secondTotal)

    bestCutIndex = min(range(n), key=cutQuality)
    leftHalf, rightHalf = sortedVertexIndices[:bestCutIndex], sortedVertexIndices[bestCutIndex:]
    return list(sorted(leftHalf)), list(sorted(rightHalf))


if __name__ == "__main__":
    theBestCut = bestCut(exampleMatrix)
    print(theBestCut)

    example2 = numpy.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            if i == j:
                continue

            if (i < 50 and j < 50) or (i >= 50 and j >= 50):
                if random.random() < 0.5:
                    example2[i, j] = 1
            else:
                if random.random() < 0.1:
                    example2[i, j] = 1

    theBestCut = bestCut(example2)
    print(theBestCut)

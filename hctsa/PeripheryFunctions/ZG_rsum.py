import numpy


def ZG_rsum(X):
    """
    """
    Z = numpy.zeros(X.shape[0])

    for i in range(X.shape[1]):
        Z = Z + X[:, i]

    return Z

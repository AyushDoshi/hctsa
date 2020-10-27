import numpy

from hctsa.Operations import DK_lagembed


def DK_timerev(x, timeLag=1):
    """
    """
    foo = DK_lagembed(x, 3, timeLag)

    a = foo[:, 0]
    b = foo[:, 1]
    c = foo[:, 2]

    res = numpy.mean(numpy.multiply(numpy.multiply(a, a), b) - numpy.multiply(numpy.multiply(b, c), c))

    return res

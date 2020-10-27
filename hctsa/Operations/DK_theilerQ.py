import numpy


def DK_theilerQ(x):
    """
    """
    x2 = numpy.mean(numpy.square(x)) ** (3 / 2)

    if x2 == 0:
        return 0

    d2 = x[0:-1] + x[1:]
    Q = numpy.mean(numpy.power(d2, 3)) / x2

    return Q

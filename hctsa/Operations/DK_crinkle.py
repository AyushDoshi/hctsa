import numpy


def DK_crinkle(x):
    """
    """
    x -= numpy.mean(x)

    x2 = numpy.mean(numpy.square(x)) ** 2

    if x2 == 0:
        return 0

    d2 = 2 * x[1:-1] - x[0:-2] - x[2:]

    return numpy.mean(numpy.power(d2, 4)) / x2

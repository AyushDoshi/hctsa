# @numba.jit(nopython=True,parallel=True)
import numpy


def EN_ShannonEn(y):
    """
    """
    p = numpy.zeros(len(numpy.unique(y)))
    n = 0
    for i in numpy.unique(y):
        p[n] = len(y[y == i]) / len(y)
        n += 1

    return -numpy.sum(p * numpy.log2(p))

# @numba.jit(nopython=True,parallel=True)
import numpy


def DN_Burstiness(y):
    """
    """
    if y.mean() == 0:
        return numpy.nan

    r = numpy.std(y) / y.mean()

    B = (r - 1) / (r + 1)

    return B

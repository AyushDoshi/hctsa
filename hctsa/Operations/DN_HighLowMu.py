# @numba.jit(nopython=True,parallel=True)
import numpy


def DN_HighLowMu(y):
    """
    """
    mu = numpy.mean(y)
    mhi = numpy.mean(y[y > mu])
    mlo = numpy.mean(y[y < mu])
    return (mhi - mu) / (mu - mlo)

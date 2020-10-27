# @numba.jit(nopython=True,parallel=True)
import numpy


def DN_TrimmedMean(y, n=0):
    """
    """
    N = len(y)
    trim = int(numpy.round(N * n / 2))
    y = numpy.sort(y)
    # return stats.trim_mean(y,n) doesn't agree with matlab
    return numpy.mean(y[trim:N - trim])

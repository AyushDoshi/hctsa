# @numba.jit(nopython=True,parallel=True)
import numpy


def DN_STD(y):
    """
    """
    # y must be numpy array
    # if not isinstance(y,numpy.ndarray):
    #     y = numpy.asarray(y)
    return numpy.std(y)

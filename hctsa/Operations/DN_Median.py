

# @numba.jit(nopython=True)
import numpy


def DN_Median(y):
    """
    """
    # y must be numpy array
    # if not isinstance(y,numpy.ndarray):
    #     y = numpy.asarray(y)
    return numpy.median(y)

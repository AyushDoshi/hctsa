# @numba.jit(nopython=True)
# Quantile function seems to be slower with numba
import numpy


def DN_Quantile(y, q=.5):
    """
    """
    # if not isinstance(y,numpy.ndarray):
    #     y = numpy.asarray(y)
    return numpy.quantile(y, q)
